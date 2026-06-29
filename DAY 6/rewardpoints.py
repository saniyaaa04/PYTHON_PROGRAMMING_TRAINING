#inhertiance
class VISAcard:
    def __init__(self,holder_name,card_number):
        self.holder_name=holder_name
        self.card_number=card_number

    def display_detail(self):
        print(self.holder_name)
        print(self.card_number)
        
    def compute_reward(self,amount):
        reward=amount*0.01
        print("The Reward for VISA card is :",reward)


class HPVISAcard(VISAcard):
    def compute_reward(self,purchase_type,amount):
        reward=amount*0.01
        if purchase_type=="Fuel":
            reward+=10
        print("The Reward for HPVISA card is :",reward)

card_type=input("Enter the cardtype HPVISA/VISA :").upper()
if card_type not in ["HPVISA","VISA"]:
    print("INVALID")
else:
    holder_name=input("Enter the name :").strip()
    card_number=input("Enter the Card Number :").strip()
    amount=float(input("Enter the amount :"))
    purchase_type=input("Enter Purchase Type :").strip()

    if card_number=="VISA":
        card=VISAcard(holder_name,card_number)
    else:
        card=HPVISAcard(holder_name,card_number)

    card.display_detail()
    card.compute_reward(purchase_type,amount)