import instaloader
mod=instaloader.Instaloader()
a=input('enter the user name')
mod.download_profile(a,profile_pic_only=True)