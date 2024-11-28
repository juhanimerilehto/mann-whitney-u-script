import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def perform_mannwhitney_analysis(excel_path='data.xlsx',
                               group_column='Group',      # Column containing group labels
                               value_column='Value',      # Column containing measurements
                               group1_name='Group1',      # Name of first group
                               group2_name='Group2',      # Name of second group
                               output_prefix='mannwhitney'):
    """
    Performs Mann-Whitney U test analysis between two independent groups.
    
    Parameters:
    -----------
    excel_path : str
        Path to Excel file containing the data
    group_column : str
        Name of column containing group labels
    value_column : str
        Name of column containing the values to compare
    group1_name, group2_name : str
        Names of the groups to compare
    output_prefix : str
        Prefix for output files
    """
    
    # Read the data
    print(f"Reading data from {excel_path}...")
    df = pd.read_excel(excel_path)
    
    # Extract the two groups
    group1_data = df[df[group_column] == group1_name][value_column]
    group2_data = df[df[group_column] == group2_name][value_column]
    
    # Perform Mann-Whitney U test
    statistic, p_value = stats.mannwhitneyu(
        group1_data, 
        group2_data,
        alternative='two-sided'
    )
    
    # Calculate effect size (r = Z / sqrt(N))
    n1, n2 = len(group1_data), len(group2_data)
    z_score = stats.norm.ppf(p_value/2)  # Two-tailed
    effect_size = abs(z_score / np.sqrt(n1 + n2))
    
    # Calculate descriptive statistics
    desc_stats = pd.DataFrame({
        'Statistic': ['Count', 'Median', 'Mean', 'Std Dev', 
                     '25th Percentile', '75th Percentile'],
        group1_name: [len(group1_data), group1_data.median(), 
                     group1_data.mean(), group1_data.std(),
                     group1_data.quantile(0.25), group1_data.quantile(0.75)],
        group2_name: [len(group2_data), group2_data.median(), 
                     group2_data.mean(), group2_data.std(),
                     group2_data.quantile(0.25), group2_data.quantile(0.75)]
    })
    
    # Create results dictionary
    results = {
        'Test Type': 'Mann-Whitney U Test',
        'U-statistic': statistic,
        'p-value': p_value,
        'Effect Size (r)': effect_size,
        'Effect Size Interpretation': interpret_effect_size(effect_size),
        'Significant': 'Yes' if p_value < 0.05 else 'No',
        'Group 1': group1_name,
        'Group 2': group2_name,
        'Group 1 Median': group1_data.median(),
        'Group 2 Median': group2_data.median()
    }
    
    # Create timestamp for file naming
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Save results to Excel
    excel_output = f'{output_prefix}_results_{timestamp}.xlsx'
    with pd.ExcelWriter(excel_output) as writer:
        pd.DataFrame([results]).to_excel(
            writer, sheet_name='Test Results', index=False
        )
        desc_stats.to_excel(
            writer, sheet_name='Descriptive Stats', index=False
        )
    
    print("\nResults saved to:", excel_output)
    
    # Create visualizations
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # 1. Box plot with individual points
    sns.boxplot(x=df[group_column], y=df[value_column], 
                order=[group1_name, group2_name], ax=ax1)
    sns.swarmplot(x=df[group_column], y=df[value_column], 
                 order=[group1_name, group2_name],
                 color='0.25', size=4, alpha=0.5, ax=ax1)
    ax1.set_title(f'Distribution Comparison\np = {p_value:.4f}')
    
    # 2. Violin plot with quartiles
    sns.violinplot(x=df[group_column], y=df[value_column],
                  order=[group1_name, group2_name],
                  inner='quartile', ax=ax2)
    ax2.set_title('Distribution Density with Quartiles')
    
    plt.tight_layout()
    
    # Save plot
    plot_output = f'{output_prefix}_plot_{timestamp}.png'
    plt.savefig(plot_output, dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Plot saved to:", plot_output)
    
    # Print results to terminal
    print("\nMann-Whitney U Test Results:")
    print("--------------------------")
    print(f"U-statistic: {statistic:.4f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Effect size (r): {effect_size:.4f}")
    print(f"Effect size interpretation: {interpret_effect_size(effect_size)}")
    print(f"Significant difference: {'Yes' if p_value < 0.05 else 'No'}")
    print("\nDescriptive Statistics:")
    print(desc_stats)

def interpret_effect_size(r):
    """
    Interprets the effect size based on Cohen's guidelines
    for correlation coefficient r
    """
    if r < 0.10:
        return 'Negligible effect'
    elif r < 0.30:
        return 'Small effect'
    elif r < 0.50:
        return 'Medium effect'
    else:
        return 'Large effect'

if __name__ == "__main__":
    # Example usage:
    # Modify these parameters according to your data
    perform_mannwhitney_analysis(
        excel_path='data.xlsx',
        group_column='Group',
        value_column='Value',
        group1_name='Control',
        group2_name='Treatment',
        output_prefix='mannwhitney'
    )