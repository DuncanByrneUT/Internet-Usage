Project Description:
An educational dashboard that visualizes and analyzes global internet usage data. This dashboard aims to:

#Provide an overview of global internet statistics, including total users and average penetration rates.
Highlight disparities in internet usage across different countries or regions.
Display growth trends in internet usage over time.
Offer educational content explaining the importance of internet access in various life aspects like education, economy, health, and social connectivity.

Technologies Used:
Python - The primary programming language for scripting and data manipulation.
Pandas for data manipulation, cleaning, and analysis.
Seaborn for creating statistical data visualizations. (We switched from Plotly to Seaborn upon your request.)
Matplotlib (which comes with Seaborn) for additional plotting capabilities if needed.
Streamlit - A Python library for creating web applications easily. It allows us to:
Create interactive user interfaces.
Embed data visualizations directly in the web app.
Implement navigation through a sidebar.


Install Dependencies:
Install the required Python packages:

pip install pandas streamlit seaborn

#Download or Prepare the Data:
Make sure you have the internet_users.csv file in a directory named CSV at the same level as your script file. https://www.kaggle.com/datasets/kanchana1990/world-internet-usage-data-2023-updated


Run the Application:
Navigate to the directory containing your script.py in the terminal or command prompt.
Run the Streamlit app with:

streamlit run script.py

This command will start a local server, and automatically open your default browser to display the dashboard.
![Screenshot 2025-01-14 at 3 57 36 PM](https://github.com/user-attachments/assets/ac8a45a1-6ea3-4de3-9cb7-852591c17452)
![Screenshot 2025-01-14 at 3 57 51 PM](https://github.com/user-attachments/assets/e42aa1a0-5eea-41bb-85eb-f519f8af6d2b)
