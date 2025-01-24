def display(data):
    print(f"the area is:{data}")
def get_input():
    recieved_length=input("length:")
    recieved_width =input("width:")
    return(recieved_length,recieved_width)
def compute_area(length,width):
    data = int(length)*int(width)
    return data
def main():
    (length,width)=get_input()
    area= compute_area(length, width)
    display(area)
main()