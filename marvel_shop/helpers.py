import requests 
import requests_cache 
import json 
import decimal

# from marvel import Marvel  #OMG WHY<--------

# m = Marvel("779573fcec789c10d27d623a2da47350",
#            "c032324b11b4993679447aff6381d33f0dbb2d5")

# def get_marvel_data(name_):
     
#      data = m.characters.all(name=name_)['data']['results'][0]
#      print(data)

#      description = data['description'] #we know this is the right path because we tested it
#      comics = data['comics'] #however you need to get to the # of comics appeared in
#      image = data['image'] #however you need to get to an image url

#      marvel_stats = {
#           'description' : description,
#           'comics' : comics,
#           'image' : image 
#      }

#      return marvel_stats #this is going to return a dictionary for that specific marvel character 

# data = m.characters.all()
# print(data)
#------------------------------------HELP----------------------------------------------------------------
#MARVEL API STUFF
# def marvel_des(name_):
     
#      data = m.characters.all(name=name_)['data']['results'][0]
#      print(data)

#      description = data['description'] #we know this is the right path because we tested it
#      comics = data['comics'] #however you need to get to the # of comics appeared in
#      image = data['image'] #however you need to get to an image url

#      marvel_stats = {
#           'description' : description,
#           'comics' : comics,
#           'image' : image 
#      }

#      return marvel_stats #this is going to return a dictionary for that specific marvel character

# def marvel_des(name_):

#     data = (characters.all(name=name_)["data"]["results"][0])
#--------------------------------------------------------------------------------
 

 
# # getting the characters object
# characters = m.characters 
 
# # serial code of your favourite character
# # this can be different according to your preference
# x = 1011334
# for n in range (0, 6): 
   
#       # search for comics of this character
#     all_characters=characters.comics(x) 
     
#     x = x+1
#     for i in range (1,12):
#       print(all_characters['data']['results'][int(i)]['title'])

#----------------------------------------------------------------------------------------
#setup our api cache location (this is going to make a temporary database storage for our api calls)

# requests_cache.install_cache('image_cache', backend='sqlite')


# def get_image(search):
#     url = "https://google-search72.p.rapidapi.com/imagesearch/"

#     querystring = {"q": search,"gl":"us","lr":"lang_en","num":"10","start":"0"}

#     headers = {
#         "X-RapidAPI-Key": "5bb8b6eab7msh7111c8bf2c05cd2p139b99jsn519fe659662c",
#         "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers, params=querystring)

#     data = response.json()
#     # print(data)

#     img_url = ""

#     if 'items' in data.keys():
#            img_url = data['items'][0]['originalImageUrl'] 

#     return img_url



class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): #if the object is a decimal we are going to encode it 
                return str(obj)
        return json.JSONEncoder(JSONEncoder, self).default(obj) #if not the JSONEncoder from json class can handle it