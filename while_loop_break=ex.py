# 😎😎😎😎😎if break statement ကို while loop ထဲမှာ သုံးမယ်ဆိုရင် loop ကို ရပ်ပစ်နိုင်ပါတယ်။

# 😎😎😎အလုပ်လုပ်ပုံ: ပထမဆုံး command ကို အလွတ် ("") စတင်သတ်မှတ်ပါတယ်။ while ထဲ ရောက်တဲ့အခါ
# command.lower() != "quit" ဆိုတာ မှန် မမှန် အရင်စစ်ပါတယ်။
# quit မဟုတ်သေးရင် အောက်က ကုဒ်တွေကို လုပ်ဆောင်ပြီး input တောင်းပါတယ်။
# quit လို့ ရိုက်လိုက်မှသာ Loop က ရပ်သွားမှာ ဖြစ်ပါတယ်။

# 😎
# command = ""
# while command.lower() != "quit":
#     command = input("Type: ")
#     print(command, "you typed")

# 😎😎 ဒုတိယပုံစံ (Infinite Loop နှင့် break သုံးခြင်း)
# ဒီပုံစံကတော့ အမြဲတမ်း မှန်နေမယ့် while True ကိုသုံးပြီး
# လိုအပ်တဲ့အခြေအနေရောက်ရင် break နဲ့ ရပ်ပစ်တာ ဖြစ်ပါတယ်
# အသုံးများပါတယ်

command = ""
while True:
    command = input("Type: ")
    print(command, "you typed")
    if command.lower() == "quit":
        break
