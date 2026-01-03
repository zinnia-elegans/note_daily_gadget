import csv

def main():
    try:
        with open('../01_data/2025-analytics.csv', 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)
    except FileNotFoundError:
        print("Error: 2025-analytics.csv not found.")
        return

    results = []
    for row in data:
        try:
            views = float(row['Views'])
            likes = float(row['Likes'])
            comments = float(row['Comments'])
            # Purchases assumed 0
            purchases = 0.0
            
            if views > 0:
                rate = ((likes + comments + purchases) / views) * 100
            else:
                rate = 0.0
                
            results.append({
                'Title': row['Title'],
                'Engagement_Rate': rate,
                'Views': int(views),
                'Likes': int(likes),
                'Comments': int(comments)
            })
        except ValueError:
            continue

    # Sort by Engagement Rate descending
    results.sort(key=lambda x: x['Engagement_Rate'], reverse=True)

    # Print header
    print(f"|Title|Engagement Rate (%)|Views|Likes|Comments|")
    print(f"|---|---|---|---|---|")
    
    # Print top 10 rows
    for row in results[:10]:
        print(f"|{row['Title']}|{row['Engagement_Rate']:.2f}|{row['Views']}|{row['Likes']}|{row['Comments']}|")

if __name__ == "__main__":
    main()
