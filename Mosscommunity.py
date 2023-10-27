# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 19:39:25 2023

@author: Husain
"""
import copy
import pg
from operator import itemgetter
import requests 
from bs4 import BeautifulSoup
import re
import streamlit as st

def main():
        
        
        file = open('from-Moss.txt', 'w')
        url = 'http://moss.stanford.edu/results/6/7588194204467/'
        response = requests.get(url)
        if response.status_code == 200:
            temp3 = ''
            i=0
            for line in response.iter_lines():
                temp2 = str(line)
                if '<TR>' in temp2:
                    temp3 = temp2.split('>')[-2][:-4] + ')\t'
                if ' <TD>' in temp2:
                    temp3 = temp3+temp2.split('>')[-2][:-4] + ')\t'
                if '<TD ' in temp2:
                    temp3 = temp3 + temp2.split('>')[-1][:-1]
                   
                    file.write(temp3 +'  '+str(i)+ '\n')
                    i+=1
                    temp3 = ''
        file.close()
        
        
        def names_lst(file):
            ''' Takes a file of  names
                returns the list of the names in the file '''
        
            moss = open(file, 'r')
            t=" "
            names_list = []
            Moss_list = []
            for line in moss:
                temp=line.split()
                #Moss_list.append(f"{temp[0]+t+temp[1] : <35}{temp[2]+t+temp[3] : <35}{temp[4] : >7}")
                Moss_list.append(line)
                names_list.append(temp[0][5:])
                names_list.append(temp[2][5:])
                
                    
            moss.close()
        
            return set(names_list),Moss_list
        
        
        names, Moss = names_lst('from-Moss.txt')
        
        names_cod={}
        i=0
        for name in names:
             names_cod[name]=i
             i+=1
        #print(len(names_cod))
        
        
            
            
        adj_lst={}
        
        for name in names:
            adj_lst[name]=[]
            for line in Moss:
                if name in line:
                    adj_lst[name].append(line)
                    
        adj_lst_cod={}
        for name in names_cod:
                st=set()
            
                for pair in adj_lst[name]:
                    
                    temp=pair.split()
                    
                    st.add(names_cod[temp[0][5:]])
                    
                    st.add(names_cod[temp[2][5:]])
           
                adj_lst_cod[names_cod[name]]=list(st)
        
        names_cod_rev={}   
        for name in names_cod:
            names_cod_rev[names_cod[name]]=name
            
          
            
        # for name in adj_lst:
        #     if len(adj_lst[name])>1:
        #         print(adj_lst[name],"\n\n")
        #print(len(Moss),names)
        adj_graph=pg.random_graph(len(adj_lst_cod),0)
        
        
        for code in adj_lst_cod:
            for cod in adj_lst_cod[code]:
                adj_graph.add_edge(code, cod)
            
        #print(adj_graph)
        
        Comps=adj_graph.components()
        # adj_graph.add_vertices(5)
        # adj_graph.add_edge(2, 3)
        #print(adj_graph.adjacency_list())
        
        # for item in Comps:
        #   if len(item)==11:
        #      print(item)            
        Comps_name=[]
        for item in Comps:
            lst=[]
            for num in item:
                lst.append(names_cod_rev[num])
            Comps_name.append(lst)
         
            
        c_wise=[]
        t=" "
        
        
        for comp in Comps_name:
            lst=[]
            for person in comp:
                for pair in Moss:
                    
                   if person in pair:
                       #print("P     :   ", pair)
                       temp=pair.split()
                       #Moss_list.append(f"{temp[0]+t+temp[1] : <35}{temp[2]+t+temp[3] : <35}{temp[4] : >7}")
                       
                       
                       lst.append(f"{temp[0][5:]+t+temp[1] : <45}{temp[2][5:]+t+temp[3] : <45}{temp[4] : >7}{temp[5] : >6}")
                      
                       
            c_wise.append((comp,list(set(lst))))
        #print(c_wise)
        
        
        #------------------------------------------------------------------------
        def moss_raw(c_wise):
                file = open("Moss_community.txt","w")  
                c=0
                for item in c_wise:
                 
                      c+=1  
                      # print("\n",c,") ",len(item[0])," : people : ",item[0],"   :%"+\
                      #       str(int(100*len(item[1])/((len(item[0])*(len(item[0])-1))/2)))+" collaboration-connectiom-copy \n\n")
                      file.write("\n"+str(c)+") "+str(len(item[0]))+" : people : ")
                      for i in item[0]:
                          file.write(" "+i+" ")
                      file.write("   : %"+str(int(100*len(item[1])/((len(item[0])*(len(item[0])-1))/2)))+" collaboration-connection-copy \n\n")
                      for x in item[1]: 
                           file.write(x)
                           file.write("\n")
                           #print(x) 
                file.close()  
        #moss_raw(c_wise)
        #--------------------------------------------------------------------------        
        c_wise_sorted1=[]
        c_wise_sorted=[]
        for item in c_wise:
         
            lst=[]
            for x in item[1]:
               temp=x.split()
               #print(temp)
               try:
                  lst.append([temp[0], temp[1], temp[2], temp[3], int(temp[4]) , int(temp[1][1:-2])+int(temp[3][1:-2]), max(int(temp[1][1:-2]),int(temp[3][1:-2])) , int(temp[-1]) ])
                  
               except IndexError or ValueError:
                   #lst.append([temp[0], temp[1][:6], temp[1][6:], temp[2], int(temp[3]) , int(temp[1][1:-2])+int(temp[2][1:-2]), max(int(temp[1][1:-2]),int(temp[3][1:-2]))  ])
                   print(temp," out of index")
            lst.sort(reverse=True, key = itemgetter(4))
            lst.sort(reverse=True, key = itemgetter(5))
            lst.sort(reverse=True, key = itemgetter(6))
            
        
               
            c_wise_sorted1.append((item[0],lst,len(item[0])))
            c_wise_sorted1.sort(reverse=True, key = itemgetter(2))
        
        
            
        for item in c_wise_sorted1:
            c_wise_sorted.append((item[0],item[1]))
        
        
        
                  
         
        
        
        #----------------------------------------------------------------------------    
        
        
        def  adj_file(adj_lst):
            
                dict_name_num_freinds={}
                file = open("adj_file.txt","w")
                
                for i,prsn in enumerate(adj_lst):
                    file.write("("+str(i+1)+"):"+prsn+" connections --> "+str(len( adj_lst[prsn]))+",")
                    dict_name_num_freinds[prsn]=str(len( adj_lst[prsn]))
                
                for i,prsn in enumerate(adj_lst):
                    file.write("\n\n"+str(i+1)+":"+prsn+" connections --> "+str(len( adj_lst[prsn]))+"\n-----------------------------------------------")
                    for item in  adj_lst[prsn]:
                        x=item.split()
                        file.write("\n"+f"{x[0]+t+x[1] : <45}{x[2]+t+x[3] : <45}{x[4] : >7}{x[5] : >7}")
                    file.write("\n---------------------------------------------------------------------------------------------------------\n")
                file.close()
                return dict_name_num_freinds
        dict_name_num_freinds = adj_file(adj_lst)
        
        
        #--------------------------------------------------------------------------------
           
        def moss_prc(c_wise_sorted, dict_name_num_freinds):
                file = open("Moss_community_prc.txt","w")
                file.write(str(len(c_wise_sorted))+" Clusters")
                c=0
                for item in c_wise_sorted:
                    
                      c+=1
                      # print("----------------------------------------------------------")
                      # print("\n",c,") ",len(item[0])," : people : ",item[0],"   :%"+\
                      #       str(int(100*len(item[1])/((len(item[0])*(len(item[0])-1))/2)))+" collaboration-connectiom-copy \n\n")
                      
                      file.write("\n###################################################\n")
                      file.write("\n"+str(c)+") "+str(len(item[0]))+" : people ) ")
                      for i,name in enumerate(item[0]):
                          
                          file.write(name+"( "+dict_name_num_freinds[name]+" )   ")
                      file.write(": %"+str(int(100*len(item[1])/((len(item[0])*(len(item[0])-1))/2)))+" = "+str(len(item[1])) +" collaboration-connection-copy \n\n")
                      file.write("\n----------------------------------------------------------\n")
                      
                      #print("----------------------------------------------------------")
                      for x in item[1]: 
                           file.write(f"{x[0]+t+x[1] : <45}{x[2]+t+x[3] : <45}{x[4] : >7}{x[-1] : >7}")
                           #file.write(x[0]+ " " +x[1]+ " "+x[2]+ " "+x[3]+ " "+str(x[4]))
                           file.write("\n\n")
                           #print(f"{x[0]+t+x[1] : <35}{x[2]+t+x[3] : <30}{x[4] : >7}")
                           #print(x[0]+ " " +x[1]+ " "+x[2]+ " "+x[3]+ " "+str(x[4])) 
                file.close()
                
        moss_prc(c_wise_sorted,dict_name_num_freinds)
        
        #print(adj_lst)
        
        
        
        
        
         
        # print("---------------------------------------------------------------------------")
        # for item in coop_list:
        #  if len(item)>2:
        #      print(item)
        #      for per in item:
        #          for pair in adj_lst[per]:
        #              print(pair)
        #  print("---------------------------------------------------------------------------")
        
if __name__ == '__main__':
  main(x='http://moss.stanford.edu/results/6/7588194204467/')        
