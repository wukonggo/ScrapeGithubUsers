import requests
from bs4 import BeautifulSoup
import time

def get_users(url):
    users = []
    for page in range(1, 201):
        response = requests.get(f"{url}?page={page}")
        soup = BeautifulSoup(response.content, 'html.parser')
        
        user_elements = soup.select('p.text-xl.text-orange-600')
        if not user_elements:
            break
        
        for element in user_elements:
            users.append(element.text.strip())
        
        print(f"Processed page {page}, found {len(user_elements)} users")
        # time.sleep(1)  # 添加延迟以避免过于频繁的请求
    
    return users

def main():
    url = "https://opensource-heroes.com/developers"
    all_users = get_users(url)

    print(f"Total users found: {len(all_users)}")
    print("First 10 users:", all_users[:10])

    # 将结果保存到文件
    with open('opensource_heroes_users.txt', 'w', encoding='utf-8') as f:
        for user in all_users:
            f.write(f"{user}\n")

    print("Results saved to opensource_heroes_users.txt")

if __name__ == "__main__":
    main()