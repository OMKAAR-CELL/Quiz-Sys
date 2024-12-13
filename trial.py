import matplotlib.pyplot as plt

def create_bar_chart():
    categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
    values = [10, 20, 15, 30]
    
    plt.figure(figsize=(8, 6))  # Set figure size
    plt.bar(categories, values)
    
    # Change the font size, font family, and font style of the x-axis tick labels (categories)
    plt.yticks(fontsize=14, fontfamily='serif', fontweight='bold')  # Change font properties
    
    plt.xlabel('Categories', fontsize=14)
    plt.ylabel('Values', fontsize=14)
    
    plt.savefig('bar_chart.png')
    plt.close()

create_bar_chart()
