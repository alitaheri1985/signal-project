# utils/vip_manager.py

VIP_USERS_FILE = "vip_users.txt"

def load_vip_users():
    try:
        with open(VIP_USERS_FILE, "r") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

def save_vip_users(vip_users):
    with open(VIP_USERS_FILE, "w") as f:
        for user_id in vip_users:
            f.write(f"{user_id}\n")

def add_vip_user(user_id):
    vip_users = load_vip_users()
    vip_users.add(str(user_id))
    save_vip_users(vip_users)

def is_vip_user(user_id):
    vip_users = load_vip_users()
    return str(user_id) in vip_users
