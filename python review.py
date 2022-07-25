def create_youtube_video(title, description):
  video = {"title":title,"description":description,     "likes" :0, "dislikes":0, "comments":{}}
  return video

def likes(video):
  if 'likes' in video:
    video["likes"] += 1
    return video
def dislikes(video):
  if 'dislikes' in video:
     video["dislikes"] +=1
     return video 
def add_comment(youtubevideo, username, commenttext):
  youtubevideo["comments"] [username] = commenttext

  return youtubevideo

video1 = create_youtube_video ("Ella's new video", "AWSOME")
for like in range (495):
  likes (video1)
  print (video1)  
