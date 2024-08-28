import csv
import random
from datetime import datetime, timedelta

def generate_customer_data(num_customers):
    customers = []
    current_date = datetime.now()
    
    for i in range(num_customers):
        customer_id = f'113GHS{i+1:04d}'
        first_name = random.choice(['Verge', 'Pratt', 'Nike', 'Brother Fii', 'Yesu', 'Sarah', 'Chris', 'Tawal', 'Halal', 'Gazprom'])
        last_name = random.choice(['Enterprise', '& Sons', 'Company Limited', '& Co.', 'LLC', 'Inc.', 'Group', 'LLP', 'Ltd.', '& Partners', 'Ventures'])
        zone = random.choice(['South', 'South-East', 'North', 'Middle Belt', 'Tema', 'Upper Middle Belt', 'West', 'North-West', 'Mines'])
        customer_name = f'{first_name} {last_name}'
        
        status = random.choice(['Active', 'Inactive'])
        
        customer_since = current_date - timedelta(days=random.randint(1, 3650))  # Up to 10 years ago
        
        if status == 'Active':
            last_activity = current_date - timedelta(days=random.randint(0, 180))  # Within last 6 months
        else:
            last_activity = current_date - timedelta(days=random.randint(181, 730))  # 6 months to 2 years ago
        
        total_purchases = round(random.uniform(30000, 500000), 2)  # Random float between 30000 and 500000
        
        customers.append([
            customer_id,
            customer_name,
            status,
            last_activity.strftime('%Y-%m-%d'),
            customer_since.strftime('%Y-%m-%d'),
            zone,
            f'{total_purchases:,.2f}'  # Format as currency
        ])
    
    return customers

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Customer ID', 'Customer Name', 'Status', 'Last Activity Date', 'Customer Since', 'Zone', 'Total Purchases'])
        writer.writerows(data)

if __name__ == '__main__':
    num_customers = 500 
    customer_data = generate_customer_data(num_customers)
    save_to_csv(customer_data, 'customer_data.csv')
    print(f'{num_customers} customer records have been generated and saved to customer_data.csv')