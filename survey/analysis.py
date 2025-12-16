'''
Created on 16. des. 2025

@author: joschua

This module is used for preparing and processing data.

'''

import os
from pathlib import PurePath
import config

import pandas as pd
import matplotlib.pyplot as plt

from visualization import plot_data
  
def prepare_data(data,group_by,lookup,kind,sep=""):
   """
   Prepares data for processing by ...
   
   TODO: What is this actually doing?
   """
   
   
   if not group_by:
      print("No paramter for grouping the data has been chosen")
      return

   if kind == "text":
      curr_data = data[group_by].dropna().to_list()
      curr_str = "\n".join(["* {}".format(i.replace("\n","").strip()) for i in curr_data])
   
   else:
      #data = data[data[group_by]!=-1] # Remove all nan
      if sep:
         #print(data[group_by].str.rstrip(sep).str.split(sep))
         data[group_by] = data[group_by].str.rstrip(sep).str.split(sep)
         #print(data)
         data           = data.explode(group_by)
      
      if "answers-repl" in lookup and group_by in lookup["answers-repl"]: # What is this?
         repl_lut = lookup["answers-repl"][group_by]
         
         data = data.replace(repl_lut)
         #data[group_by] = list(map(lambda x: repl_lut[x], data[group_by]))
      
      curr_data = data.groupby(group_by)[group_by].count()
      curr_data = curr_data.to_frame()
      
      curr_str = "{}".format(curr_data)
      
   return curr_data, curr_str
  
def process_data():
   """
   Proceses data by ...
   
   TODO: What is this actually doing?
   """
   
   data_file = os.path.join("data","2025-12-10_Svar-paa-sporreundersokelsen-om-curb-cut-effekten-i-dataspill.csv")
   if not os.path.exists(data_file):
      print("The file could not be found: \"{}\".".format(data_file))
      return
   
   """
   *** Analysis ***
   
   1. Defining data sets.
   """
   # I think this is the cleanest way but I encourage you to prove me wrong.
   df_all = pd.read_csv(data_file,sep=";")
   df_all.replace(r'\\n', '\n', regex=True, inplace=True)
   #df_norway_only  = df_all[df_all["land"] == "Ukjent"]
   #df_sweden_only  = df_all[df_all["land"] != "Ukjent"]
   
   """
   2. Defining tasks for the analysis.
   """
   lan = "no"
   tasks = config.tasks[lan]
   
   """
   3. Defining basic lookup variables.
   
   Lookup is used for ???. [Needs to be explained.]
   """
   lookup = config.lookup[lan]
   
   # I think this is the cleanest way but I encourage you to prove me wrong.
   lookup["data_set"] = {
   #   "no": df_norway_only,
   #   "se": df_sweden_only,
      "all": df_all
      }
   
   """
   4. Conducting the analysis
   """
   res_file = "" # Will be initiated later
   res_str = "# Results from the survey" # All results will be stored in a text file, next to th graphs.
   
   res_dict = {} # Make one individual result file for each set
   
   for key,values in tasks.items():
      
      """
      Checking if necessary parameters are present.
      """
      if not "kind" in values or not values["kind"]:
         print("No plot type has been chosen.")
         continue
      kind = values["kind"]
      
      if not kind == "header":
         
         if not "var" in values or not values["var"]:
            print("No variable has been chosen.")
            continue
         var  = values["var"][0] # Why [0]?
      
      if not "sets" in values or not values["sets"]:
         print("No set(s) has(have) been chosen.")
         continue
      
      """
      Checking if optional parameters are present.
      """     
      title = ""
      if "title" in values:
         title = values["title"]
         #res_str += "\n\n## {}".format(title)
         
      niveau = 2 # Defines the niveau of the title, 2 by default, i.e. "##"
      if "niveau" in values:
         niveau = values["niveau"]
            
      """
      Processing data for each set.
      """   
      for set in values["sets"]:
         
         if not set in lookup["data_set"]:
            print("No data set exists for {}.".format(set))
            continue
         curr_data_set = lookup["data_set"][set]
         
         #TODO: This should be a separate function initiate_res_dict
         if set not in res_dict:
            res_dict[set] = {}
            res_dict[set]["str"]  = res_str # From here on we are just going to use the res_str from the dictionary 
            res_dict[set]["file"] = os.path.join("RESULTS-{}_{}".format(set,lan).upper()+".md")
         
         # TODO: This fix is quick and dirty. Should be improved and made more robust.
         curr_title = title.replace("\n"," ")
         res_dict[set]["str"] = res_dict[set]["str"] + "\n\n{} {}. {}".format(niveau*"#",key,curr_title)
         
         if kind == "header":
            continue # For headers, just move to next key.
            
         if  not "subsets" in values or not values["subsets"]:   
            values, res_dict = processing_simple_set(lan,key,values,set,curr_data_set,res_dict,var,kind,lookup)
         else:
            values, res_dict = processing_multiple_subsets(lan,key,values,set,curr_data_set,res_dict,var,kind,lookup)
   
   """
   5. Writing the results to a text file.
   """
   for set,values in res_dict.items():
      if not "str" in values:
         print("No results have been recorded for set \"{}\"".format(set))
      
      if not "file" in values:
         print("No save file has been chosen for set \"{}\"".format(set))
      
      res_str  = values["str"]
      res_file = values["file"]
      
      with open(res_file,"w",encoding="utf-8") as outfile:
         outfile.write(res_str)   
      
      print("Results for set \"{}\" have been saved in {}.".format(set,res_file))
      
def processing_simple_set(lan,key,values,set,curr_data_set,res_dict,var,kind,lookup):
   
   target_folder = ""
   if "target-folder" in values:
      target_folder = values["target-folder"]
      
   """
   Optional parameters
   """
   sep = ""
   if "data-sep" in values:
      sep = values["data-sep"]
    
   ext       = "png"
   fig_size  = ()
   if "fig_size" in values:
      fig_size = values["fig_size"]
   
   is_percentage       = False
   if "is-percentage" in values:
      is_percentage = values["is-percentage"]
      
   cmap = ""
   if "cmap" in values:
      cmap = values["cmap"]
      
   text_bckgrd = False
   if "text_bckgrd" in values:
      text_bckgrd = values["text_bckgrd"]
  
   # TODO: What is this doing?
   title = ""
   if "title" in values:
      title = values["title"]
   
   curr_title    = title
   tmp_title     = ""
   if set in lookup["title-app"]:
      tmp_title  = lookup["title-app"][set]
   else:
      tmp_title   = set
   res_dict[set]["str"]  = res_dict[set]["str"] + "\n" # TODO: Why? What is this doing?
   
   # TODO: Is this really necessary then?
   appendix = ""
   if not appendix:
      save_file = os.path.join("results",lan,target_folder,"{:02d}-{}.{}".format(key,var,ext))
   else:
      save_file = os.path.join("results",lan,target_folder,"{:02d}-{}-{}.{}".format(key,var,appendix,ext))
      
   niveau = 2 # Defines the niveau of the title, 2 by default, i.e. "##"
   if "niveau" in values:
      niveau = values
   
   """
   Preparing data
   """
   grouped_data, curr_res = prepare_data(curr_data_set,var,lookup,kind,sep)
   
   if kind == "text":
      res_dict[set]["str"] = res_dict[set]["str"] + "\nAntall svar: {}\n\n{}".format(len(grouped_data),curr_res)
   else:
      plot_data(grouped_data,kind,curr_title,save_file=save_file,is_percentage=is_percentage,fig_size=fig_size,cmap=cmap,text_bckgrd=text_bckgrd) # Here, the actually analysis is triggered
   
      rel_save_file = os.path.relpath(save_file,os.path.dirname(res_dict[set]["file"]))
      rel_save_file = PurePath(rel_save_file).as_posix()
      
      res_dict[set]["str"] = res_dict[set]["str"] + "\n![{}]({})\n\n".format(curr_title.replace('\n',' '),rel_save_file)
      
      if not is_percentage:
         res_dict[set]["str"] = res_dict[set]["str"] + "```\n{}\n```".format(curr_res)
         
   return values, res_dict

def processing_multiple_subsets(lan,key,values,set,curr_data_set,res_dict,var,kind,lookup):
   
   target_folder = ""
   if "target-folder" in values:
      target_folder = values["target-folder"]
   
   """
   Optional parameters
   """
   sep = ""
   if "data-sep" in values:
      sep = values["data-sep"]
    
   ext       = "png"
   fig_size  = ()
   if "fig_size" in values:
      fig_size = values["fig_size"]
   
   is_percentage       = False
   if "is-percentage" in values:
      is_percentage = values["is-percentage"]
      
   cmap = ""
   if "cmap" in values:
      cmap = values["cmap"]
      
   text_bckgrd = False
   if "text_bckgrd" in values:
      text_bckgrd = values["text_bckgrd"]
  
   # TODO: What is this doing?
   title = ""
   if "title" in values:
      title = values["title"]
   
   curr_title    = title
   tmp_title     = ""
   if set in lookup["title-app"]:
      tmp_title  = lookup["title-app"][set]
   else:
      tmp_title   = set
   res_dict[set]["str"]  = res_dict[set]["str"] + "\n" # TODO: Why? What is this doing?
   
   # TODO: Is this really necessary then?
   appendix = ""
   if not appendix:
      save_file = os.path.join("results",lan,target_folder,"{:02d}-{}.{}".format(key,var,ext))
   else:
      save_file = os.path.join("results",lan,target_folder,"{:02d}-{}-{}.{}".format(key,var,appendix,ext))
   
   niveau = 2 # Defines the niveau of the title, 2 by default, i.e. "##"
   if "niveau" in values:
      niveau = values
   
   for subset_key,subset_values in values["subsets"].items(): # values["subsets"] is supposed a dict
      #print(subset_values)
      if not "var" in subset_values:
         print("No variable has been chosen for the subset.")
         continue
      var_subset = subset_values["var"]
      
      subset_appendix = ""
      if appendix:
         subset_appendix = appendix+"-"
      if not "file-app" in subset_values or subset_values["file-app"]:
         subset_appendix += "{}".format(subset_values["file-app"])
      else:
         subset_appendix += "subset-{}".format(subset_key)
      
      curr_subset_title = curr_title
      tmp_subset_title  = ""
      if not "title-app" in subset_values or not subset_values["title-app"]:
         tmp_subset_title = "subset {}".format(subset_key)
      else:
         tmp_subset_title = subset_values["title-app"]
      curr_subset_title += ", {}".format(tmp_subset_title)
      res_dict[set]["str"] = res_dict[set]["str"] + "\n{} Subset {}\n".format((niveau+1)*"#",tmp_subset_title) # This needs to be changed maybe
      
      curr_data_subset    = curr_data_set
      grouped_data_subset = []
      if not "operators" in subset_values or not subset_values["operators"]:
         print("No operator and/or value has been chosen for the subset. Using the whole data set.")
         grouped_data_subset, curr_res = prepare_data(curr_data_subset,var,lookup,kind,sep)
      
      else:
         multiple_groups = []
         for operator in subset_values["operators"]:
            if operator[0] == "equal to":
               curr_data_subset = curr_data_set[curr_data_set[var_subset]==operator[1]]
            elif operator[0] == "not equal to":
               curr_data_subset = curr_data_set[curr_data_set[var_subset]!=operator[1]]
            else:
               print("Unknown operator chosen for the subset: {}".format(operator[0])) 
               continue
            curr_grouped_data_subset, curr_res = prepare_data(curr_data_subset,var,lookup,kind,sep)
            #curr_grouped_data_subset = curr_grouped_data_subset.to_frame()
            
            if len(operator)>2:
               old_column = curr_grouped_data_subset.columns[0]
               new_column = operator[2]
               curr_grouped_data_subset = curr_grouped_data_subset.rename({old_column: new_column},axis="columns")
            multiple_groups.append(curr_grouped_data_subset)
         
         grouped_data_subset = pd.concat(multiple_groups,axis=1)
         curr_res = "{}".format(grouped_data_subset)
         
         if "is-percentage" in subset_values:
            is_percentage = subset_values["is-percentage"]
      
      target_folder = ""
      if "target-folder" in values:
         target_folder = values["target-folder"]
      sub_target_folder = ""
      if "target-folder" in subset_values:
         sub_target_folder = subset_values["target-folder"]
         
      save_file = os.path.join("results",lan,target_folder,sub_target_folder,"{:02d}-{:02d}-{}-{}.{}".format(key,subset_key,var,subset_appendix,ext))
      
      grouped_data_subset = grouped_data_subset#.dropna()
      if not kind == "text":
         plot_data(grouped_data_subset,kind,curr_subset_title,save_file=save_file,is_percentage=is_percentage,fig_size=fig_size,cmap=cmap,text_bckgrd=text_bckgrd) # Here, the actually analysis is triggered
      
         rel_save_file = os.path.relpath(save_file,os.path.dirname(res_dict[set]["file"]))
         rel_save_file = PurePath(rel_save_file).as_posix()
      
         res_dict[set]["str"] = res_dict[set]["str"] + "\n![{}]({})\n".format(curr_subset_title.replace('\n',''),rel_save_file)
      
         if not is_percentage:
            res_dict[set]["str"] = res_dict[set]["str"] + "\n```\n{}\n```\n".format(curr_res)
   
   return values, res_dict