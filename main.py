"""
Main Functions
"""
import polars as pl
import matplotlib.pyplot as plt

def load_dataset_pl(file_path):
    """
    Load the dataset using Polars.
    """
    dataframe = pl.read_csv(file_path)
    return dataframe

def general_describe_pl(dataframe, column_name):
    """
    Generate descriptive statistics for a specific column using Polars.
    """
    return dataframe.select([
        pl.col(column_name).mean().alias("mean"),
        pl.col(column_name).median().alias("median"),
        pl.col(column_name).std().alias("std"),
        pl.col(column_name).min().alias("min"),
        pl.col(column_name).max().alias("max"),
        pl.col(column_name).quantile(0.25).alias("25%"),
        pl.col(column_name).quantile(0.75).alias("75%")
    ]).to_dict(as_series=False)

def generate_vis_pl(dataframe, x_col, y_col):
    """
    Generate a scatter plot for two variables to visualize their relationship using Matplotlib.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(dataframe[x_col].to_numpy(), dataframe[y_col].to_numpy(), color='green', alpha=0.6)
    plt.title(f'{x_col} vs {y_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.show()

def generate_dist_pl(dataframe, column_name):
    """
    Generate a histogram to visualize the distribution of a variable using Matplotlib.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(dataframe[column_name].to_numpy(), bins=15, color='green', edgecolor='black')
    plt.title(f'Distribution of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def visualize_boxplot_pl(dataframe, column_name):
    """
    Generate a boxplot to summarize the distribution of a variable using Matplotlib.
    """
    plt.boxplot(dataframe[column_name].to_numpy(), vert=False, patch_artist=True, showmeans=True, 
                boxprops=dict(facecolor='lightcoral'), 
                flierprops=dict(markerfacecolor='green', marker='o'))

    plt.title(f'Box Plot of {column_name}')
    plt.xlabel(column_name)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    dataset_path = "StudentPerformanceFactors.csv"
    column_to_analyze = "Hours_Studied"

    # Load the dataset
    df_data = load_dataset_pl(dataset_path)

    # Generate summary statistics
    summary_stats_data = general_describe_pl(df_data, column_to_analyze)


    # Perform visualizations (Optional: you can comment out if not needed)
    generate_vis_pl(df_data, "Hours_Studied", "Exam_Score")
    generate_dist_pl(df_data, column_to_analyze)
    visualize_boxplot_pl(df_data, column_to_analyze)