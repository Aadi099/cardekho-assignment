
import matplotlib.pyplot as plt
import seaborn as sns
import io

def plot_graph(df, x_col, y_col, graph_type="line"):
    plt.figure(figsize=(6,4))
    if graph_type == "line":
        sns.lineplot(data=df, x=x_col, y=y_col)
    elif graph_type == "bar":
        sns.barplot(data=df, x=x_col, y=y_col)
    elif graph_type == "scatter":
        sns.scatterplot(data=df, x=x_col, y=y_col)
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return img
