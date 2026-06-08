from bale_api import BaleClient


client = BaleClient()

success, result = client.send_message("Test!")

if success:
    print("✅ Message sent")
    print(result)
else:
    print("❌ Error")
    print(result)
