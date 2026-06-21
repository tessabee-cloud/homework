import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

USER_IDS = [1, 2, 3, 4, 5]

def fetch_posts(user_id):
    url = f'https://jsonplaceholder.typicode.com/posts?userId={user_id}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def count_posts(all_posts):
    counts = {}
    for posts in all_posts:
        if posts:
            user_id = posts[0]['userId']
            counts[user_id] = len(posts)
    return counts

def find_longest_post(all_posts):
    longest_post = None
    max_length = 0
    for posts in all_posts:
        for post in posts:
            length = len(post['body'])
            if length > max_length:
                max_length = length
                longest_post = post
    return longest_post, max_length

def average_title_length(all_posts):
    total_length = 0
    total_count = 0
    for posts in all_posts:
        for post in posts:
            total_length += len(post['title'])
            total_count += 1
    return total_length / total_count if total_count > 0 else 0

def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        all_posts = list(executor.map(fetch_posts, USER_IDS))

    with ProcessPoolExecutor() as executor:
        future_count = executor.submit(count_posts, all_posts)
        future_longest = executor.submit(find_longest_post, all_posts)
        future_avg = executor.submit(average_title_length, all_posts)

        counts = future_count.result()
        longest_post, max_len = future_longest.result()
        avg_len = future_avg.result()

    print("=" * 40)
    print("        პოსტების ანალიზი")
    print("=" * 40)
    print(f"{'მომხმარებელი':<15}პოსტების რაოდენობა")
    print("-" * 36)
    for user_id in USER_IDS:
        print(f"User {user_id:<10} {counts.get(user_id, 0)}")

    print("\nყველაზე გრძელი პოსტი:")
    print(f"  მომხმარებელი: User {longest_post['userId']}")
    print(f"  სათაური: \"{longest_post['title']}\"")
    print(f"  სიგრძე: {max_len} სიმბოლო")

    print(f"\nსათაურების საშუალო სიგრძე: {avg_len:.1f} სიმბოლო")
    print("=" * 40)

if __name__ == "__main__":
    main()
