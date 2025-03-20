from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import os,json,uvicorn

# Run the App using "uvicorn app:app --reload"

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    id: int
    data: str
    flag: bool


ToDoList= []

try:
    ToDoList=json.load(open('data.json'))
except:
    print("No file")

# def retrieve_file_data():
#     try:
#         with open('todo.txt','r') as f:
#             contents=f.read()
#             arrayOfItems=contents.strip('\n')
#             for each in arrayOfItems:
#                 id,data,flag=arrayOfItems.strip('|')
#                 ToDoList.append({
#             "id":int(id),
#             "data":str(data),
#             "flag":bool(flag)
#     })

#     except IOError:
#         print("Error")


# def create_file(filename,id,data,flag):
#     try:
#         with open(filename, 'w') as f:
#             f.write(str(id)+'|'+str(data)+'|'+str(flag)+'\n')
#         print("File " + filename + " created successfully.")
#     except IOError:
#         print("Error: could not create file " + filename)


@app.get("/")
def read_root():
    try:
        ToDoList=json.load(open('data.json'))
    except:
        print("No file")
    return ToDoList

@app.delete("/{item_id}")
async def delete_item(item_id: int):
    for each in ToDoList:
        if(each['id']==item_id):
            ToDoList.remove(each)
            with open('data.json','w') as outfile:
                json.dump(ToDoList,outfile)
            return ToDoList
    return ToDoList
    

@app.post("/")
async def create_item(item: Item):   
    keyID=item.id
    print(item)
    for each in ToDoList:
        if(each['id']==item.id):
            each['data']=item.data
            each['flag']=item.flag
            with open('data.json','w') as outfile:
                json.dump(ToDoList,outfile)
            return ToDoList
    ToDoList.append({
            "id":item.id,
            "data":item.data,
            "flag":item.flag
    })
    with open('data.json','w') as outfile:
        json.dump(ToDoList,outfile)
    return ToDoList

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5050, reload=True)