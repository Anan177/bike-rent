import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.cluster import KMeans
import scipy.stats as stats
import copy
sns.set(style='darkgrid')

all_df = pd.read_csv("day.csv")
tipe_tanggal = ['dteday']
for i in tipe_tanggal:
    all_df[i] = pd.to_datetime(all_df[i])

seasonal_orders_df = all_df.groupby(by='season').agg({'cnt':'sum','atemp':'mean'}).reset_index()
seasonal_orders_df.rename(columns={"cnt": "rent_count",'atemp':'feeling temperature'}, inplace=True)
def num_to_season(x):
    if x == 1:
        return "Springer"
    elif x == 2:
        return "Summer"
    elif x == 3:
        return "Fall"
    elif x == 4:
        return "Winter"
seasonal_orders_df['season'] = seasonal_orders_df['season'].apply(num_to_season)


monthly_orders_df = all_df.groupby(by='mnth').agg({'cnt':'sum','atemp':'mean'}).reset_index()
monthly_orders_df.rename(columns={"cnt": "rent_count",'atemp':'feeling temperature'}, inplace=True)

X = copy.copy(monthly_orders_df)

def num_to_month(x):
    if x == 1:
        return "Jan"
    elif x == 2:
        return "Feb"
    elif x == 3:
        return "Mar"
    elif x == 4:
        return "Apr"
    elif x == 5:
        return "Mei"
    elif x == 6:
        return "Jun"
    elif x == 7:
        return "Jul"
    elif x == 8:
        return "Agu"
    elif x == 9:
        return "Sep"
    elif x == 10:
        return "Okt"
    elif x == 11:
        return "Nov"
    elif x == 12:
        return "Des"
monthly_orders_df['mnth'] = monthly_orders_df['mnth'].apply(num_to_month)




with st.sidebar:
    st.image("https://img.freepik.com/premium-vector/red-bike-rental-logo-with-map-pin-concept-biking-bycicle-sale-rent-bike-trip-company-mark-repair-isolated-white-background-flat-style-trend-modern-logotype-design-vector-illustration_117142-390.jpg")
    opsi = st.selectbox(
        label="Select the options you want to see",
        options=('Summary For All Season', 'Work Day vs Weekend and Holiday'))
    
if opsi== 'Summary For All Season':
    st.header('Bike Rental Summary Dashboard :sparkles:')
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total orders", value=f'{seasonal_orders_df.rent_count.sum():,}')
    with col2:
        st.metric("Time Period", value='2011-2012')

    #SEASONAL PLOT
    st.subheader('Seasonal Rent')

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 17))
    colors = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"]
    sns.barplot(
        x="season", 
        y="rent_count",
        data=seasonal_orders_df,
        palette=colors, ax=ax[0])
    ax[0].set_title("Number of Bike Rented by Season", loc="center", fontsize=50)
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].tick_params(axis='x', labelsize=35)
    ax[0].tick_params(axis='y', labelsize=30)
    ax[0].ticklabel_format(style='plain', axis='y')
    
    plt.plot(
        seasonal_orders_df["season"],
        seasonal_orders_df["feeling temperature"],
        marker='o', 
        linewidth=10,
        color="#72BCD4"
        )
    ax[1].set_title("Feeling Temperature by Season", loc="center", fontsize=50)
    ax[1].tick_params(axis='x', labelsize=35)
    ax[1].tick_params(axis='y', labelsize=30)
    ax[1].ticklabel_format(style='plain', axis='y')
    ax[1].set_ylim(0, 0.7)

    st.pyplot(fig)

    #MONTHLY PLOT
    st.subheader('Monthly Rent')
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 17))
    sns.barplot(
        x="mnth", 
        y="rent_count",
        data=monthly_orders_df,
        ax=ax[0])
    ax[0].set_title("Number of Bike Rented by Month", loc="center", fontsize=50)
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].tick_params(axis='x', labelsize=35)
    ax[0].tick_params(axis='y', labelsize=30)
    ax[0].ticklabel_format(style='plain', axis='y')
    
    plt.plot(
        monthly_orders_df["mnth"],
        monthly_orders_df["feeling temperature"],
        marker='o', 
        linewidth=10,
        )
    ax[1].set_title("Feeling Temperature by Month", loc="center", fontsize=50)
    ax[1].tick_params(axis='x', labelsize=35)
    ax[1].tick_params(axis='y', labelsize=30)
    ax[1].ticklabel_format(style='plain', axis='y')
    ax[1].set_ylim(0, 0.8)
    st.pyplot(fig)

    #SCATTER PLOT
    fig, ax = plt.subplots(figsize=(35, 17))

    sns.regplot(x='feeling temperature', y='rent_count', data=monthly_orders_df, ax=ax,scatter_kws={'s': 500})
    ax.set_title("Feeling Temprature vs. Rent Count ", loc="center", fontsize=50)
    ax.set_ylabel('Rent Count',fontsize=35)
    ax.set_xlabel('Feeling Temperature',fontsize=35)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)

    st.pyplot(fig)

    #CLUSTERING PLOT

    st.subheader('Feeling Temperature vs. Rental Count Clustering')

    kmeans = KMeans(n_clusters=3,random_state=1)
    X["Cluster"] = kmeans.fit_predict(X)
    X["Cluster"] = X["Cluster"].astype("category")
    X['Cluster'].replace([2], 'Low', inplace=True)
    X['Cluster'].replace([1], 'Mid', inplace=True)
    X['Cluster'].replace([0], 'High', inplace=True)

    fig, ax = plt.subplots(figsize=(35, 17))

    sns.set(style='darkgrid')
    ax = sns.scatterplot(data=X, 
                x="feeling temperature", 
                y="rent_count", 
                hue="Cluster",s=500)
    ax.set_title('Montly Feeling Temprature vs. Rent Count with K-Means Clustering',loc="center", fontsize=50)
    ax.set_ylabel('Rent Count',fontsize=35)
    ax.set_xlabel('Feeling Temperature',fontsize=35)
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)

    handler, label = ax.get_legend_handles_labels()
    label[0], label[2] = label[2], label[0]
    handler[0], handler[2] = handler[2], handler[0]
    legend = ax.legend(handler, label)
    for text in legend.texts:
        text.set_fontsize(40)

    st.pyplot(fig)


    X['mnth'] = X['mnth'].apply(num_to_month)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('Low Rental Category')
        Kategori1 =  X.query("Cluster == 'Low'")['mnth']
        st.subheader(", ".join(Kategori1))
    
    with col2:
        st.markdown("Mid Rental Category")
        Kategori2 = X.query("Cluster == 'Mid'")['mnth']
        st.subheader(", ".join(Kategori2))
     
    with col3:
        st.markdown("High Rental Category")
        Kategori3 = X.query("Cluster == 'High'")['mnth']
        st.subheader(", ".join(Kategori3))

elif opsi== 'Work Day vs Weekend and Holiday':
    st.header('Bike Rental Summary Dashboard :sparkles:')
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total orders", value=f'{seasonal_orders_df.rent_count.sum():,}')
    with col2:
        st.metric("Time Period", value='2011-2012')
    
    seasonal_df = all_df.groupby(by=['season','workingday']).agg({'casual':'sum','registered':'sum','cnt':'sum'})
    seasonal_df.rename(columns={"cnt": "Rent_Total",'casual':'Casual_Users','registered':'Registered_Users'}, inplace=True)

    work_day_df = seasonal_df.drop(index=0, level=1).reset_index()
    no_work_day_df = seasonal_df.drop(index=1, level=1).reset_index()

    sns.set(style="darkgrid")

    xs = ["Springer", "Springer", "Summer", "Summer", "Fall", "Fall", "Winter", "Winter"]
    hue = ["Casual_Users", "Registered_Users"] * 4

    def casual_registered_num(x):
        list_ys=[]
        for i in range(len(x)):
            a = x.iloc[i]['Casual_Users']
            b = x.iloc[i]['Registered_Users']
            list_ys.append(a)
            list_ys.append(b)
        return list_ys

    ys_1 = casual_registered_num(work_day_df)
    ys_2 = casual_registered_num(no_work_day_df)

    st.subheader('Workdays vs. Holidays and Weekends')
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 17))
    sns.barplot(x=xs, y=ys_1, hue=hue, ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].set_title("Work Day", loc="center", fontsize=50)
    ax[0].tick_params(axis ='y', labelsize=35)
    ax[0].tick_params(axis ='x', labelsize=30)
    ax[0].ticklabel_format(style='plain', axis='y')
    ax[0].set_ylim(0, 700000)
    ax[0].legend(loc='upper right',fontsize='30',)

    sns.barplot(x=xs, y=ys_2, hue=hue, ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].set_title("Weekend and Holiday", loc="center", fontsize=50)
    ax[1].tick_params(axis ='y', labelsize=35)
    ax[1].tick_params(axis ='x', labelsize=30)
    ax[1].ticklabel_format(style='plain', axis='y')
    ax[1].set_ylim(0, 700000)
    ax[1].legend(loc='upper right',fontsize='30',)

    st.pyplot(fig)

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 17))
    category = ("Casual_Users", "Registered_Users")

    total_casual_no_work = no_work_day_df.Casual_Users.sum()
    total_registered_no_work = no_work_day_df.Registered_Users.sum()
    jumlah_no_work = (total_casual_no_work, total_registered_no_work)

    total_casual_work = work_day_df.Casual_Users.sum()
    total_registered_work = work_day_df.Registered_Users.sum()
    jumlah_work = (total_casual_work, total_registered_work)

   
    ax[0].pie(jumlah_work, labels=category, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 35})
    ax[0].set_title(" ", loc="center", fontsize=50)
    ax[0].axis('equal')

    ax[1].pie(jumlah_no_work, labels=category, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 35})
    ax[1].set_title(" ", loc="center", fontsize=50)
    ax[1].axis('equal')

    st.pyplot(fig)