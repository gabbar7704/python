d=int(input("enter distance travelled in km:"))
m=int(input("enter time taken to travel the distance only min part"))
s=int(input("enter time taken to travel the distance onlysec part"))
tt=float(m*60 +s)/3600
DM=float(d)/1.61
at=tt/DM
v=DM/tt
print(f"avg time in hr taken to travel a mile:{at}")
print(f"avg velocity in mile per hour to travel.{v}")