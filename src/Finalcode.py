
import matplotlib.pylab as plt
import pandas as pd
from abc import ABC, abstractmethod
class Analysis(ABC):
    @abstractmethod
    def  PerformAnalysis():
        pass

#1
Max_Years = 13  # Number of distinct publication years expected
Bar_Colors = ['salmon', 'skyblue', 'gold', 'orange', 'violet', 'red', 'lightgrey',
              'lightcoral', 'blue', 'khaki', 'lightgreen', 'pink', 'aquamarine']

class PublicationTrend(Analysis):  # Count of books published per year
    def PerformAnalysis(self):
        # Read book dataset from CSV
        df = pd.read_csv('Books.csv')

        # Group by publication year and count books
        publication_counts = df.groupby('publication date').size().reset_index(name='Count of Books')
        print(publication_counts)

        # Prepare bar chart: publication year on X-axis, count on Y-axis
        colors = BAR_COLORS[:len(publication_counts)]
        plt.bar(publication_counts['publication date'], publication_counts['Count of Books'], color=colors)
        plt.title('Number of Books Published Per Year')
        plt.xlabel('Year of Publishment')
        plt.ylabel('Books Count')
        plt.yticks(rotation=90)
        plt.tight_layout()
        plt.show()
    

#2
Top_Max_Authors = 5  # Number of top authors to analyze

class TopFive(Analysis): # Top 5 Most Prolific Authors (Authors with the highest number of books)
    def  PerformAnalysis(self): 
        df1 = pd.read_csv('Books.csv')
        df2 = df1.groupby (['author']).size().reset_index(name='Top Five Authors') 
        print(df2)
        df3 = df2.nlargest(Top_Max_Authors,'Top Five Authors') # restrict to top 5 authors
        print (df3)
        
        # Draw Bar Chart - Authors on X Axis, Count on Y Axis
        plt.bar(df3['author'], df3['Top Five Authors'], color=['blue', 'lightgreen', 'pink', 'yellow', 'purple'])
        plt.title('Top 5 Most Profilic Authors')
        plt.xlabel('Authors')
        plt.ylabel('Count')
        plt.show()
#3
class LanguageDistribution(Analysis): #Language Distribution of Books.
    def  PerformAnalysis(self):
        df1 = pd.read_csv('Books.csv')
        df2 = df1.groupby (['language']).size().reset_index(name='Language Distribution')  
        print(df2)
        
        # Draw Bar Chart - Languages on X Axis, Count of Books on Y Axis                     
        plt.bar (df2['language'], df2['Language Distribution'],color=['khaki','blue','red','green','purple','yellow'] )
        plt.title('Language Distribution of Books')
        plt.xlabel('Language Published')
        plt.ylabel('Count of Books')
        plt.show()

#4
class Publisher(Analysis):  # Publishers by number of books published
    def PerformAnalysis(self):
        df1 = pd.read_csv('Books.csv')
        df2 = df1.groupby(['book publisher']).size().reset_index(name='Books Published by each Publisher')
        df2 = df2.sort_values(by='Books Published by each Publisher', ascending=False).head(10)  
        print(df2)
        
        plt.figure(figsize=(10, 6))
        plt.bar(df2['book publisher'], df2['Books Published by each Publisher'], color='black')
        plt.title('Publishers by Number of Books Published')
        plt.xlabel('Publisher Name')
        plt.ylabel('Count of Books')
        plt.xticks(rotation=45, ha='right')  # Slight rotation for clarity
        plt.tight_layout()
        plt.show()

#5        
class  MissingISBN (Analysis): # Percentage of records without an ISBN
    def PerformAnalysis(self):
            df1 = pd.read_csv('Books.csv')
            null_count = df1['ISBN'].isnull().sum()  # count rows where ISBN is null
            print('Count of null values in ISBN column: ', null_count)
            row_count = len(df1)  # count all rows
            print('Number of rows:', row_count)
            per = null_count/row_count*100
            print ('Percentage of null records is: ', per)
            non_null_count = df1['ISBN'].notnull().sum()
            print(non_null_count)
            
            # Values and labels
            values = [null_count, non_null_count]
            labels = ['Null Records without ISBN', 'Not Null Records with ISBN']
            # Plot pie chart
            plt.figure(figsize=(5, 5))
            plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['blue', 'yellow'])
            plt.title('Percentage of Records without ISBN')
            plt.axis('equal')  # Equal aspect ratio ensures the pie is circular
            plt.show()


#6            
class  PerYearbyLanguage (Analysis): # Number of books published per year categorized by language.
    def PerformAnalysis(self):
            df1 = pd.read_csv('Books.csv')
            # Group by two columns and get size (count of rows per group)
            df2 = df1.groupby(['publication date', 'language']).size().reset_index(name='Count Published per Year by Language')
            # Pivot for a grouped bar chart
            df3 = df2.pivot(index='publication date', columns='language', values='Count Published per Year by Language').fillna(0)
            print ('Number of Books published - Per Year By Language')
            print (df3)
            # Plot Bar Chart
            df3.plot(kind='bar')
            # Formatting
            plt.title('Number of books published per Year categorized by Language.')
            plt.xlabel('Published Year')
            plt.ylabel('Number of Books')
            plt.legend(title='Language')
            plt.tight_layout()
            plt.show()

class  Process_Strategy:
    def  ExecuteStrategy( self, analysis_obj ):
        analysis_obj.PerformAnalysis()
 
            
class  Strategy_Selector:                                           
    def  OpenMenu(self):
        while (True):
            print ("Please Select a Number to Perform the Analysis")
            print ("1 - Publication Trends Over Time (Count of Books published per year)")
            print ("2 - Top 5 Most Prolific Authors (Authors with the highest number of books )")
            print ("3 - Language Distribution of books")
            print ("4 - Number of books published by each publisher ")
            print ("5 - Missing ISBN Analysis (Count and Percentage of records without an ISBN.)")
            print ("6 - Number of books published per year categorized by language.")
            print ("7 - Exit.")
            choice = int ( input ("Enter Choice [1|2|3|4|5|6|] "))
            if (choice<1  or choice>7):
                print ("Invalid Choice")
            else:
                ps = Process_Strategy()
                if (choice==1):
                    pt     = PublicationTrend()
                    ps.ExecuteStrategy(pt)
                if (choice ==2):
                     tf = TopFive()
                     ps.ExecuteStrategy(tf) 
                if (choice ==3):
                    ld = LanguageDistribution()
                    ps.ExecuteStrategy(ld)
                if (choice ==4):
                    p = Publisher()
                    ps.ExecuteStrategy(p)
                if (choice ==5):
                    mi =  MissingISBN()
                    ps.ExecuteStrategy(mi)
                if (choice ==6):
                    pyl = PerYearbyLanguage() 
                    ps.ExecuteStrategy(pyl)    
                if (choice ==7):
                    print ("----------Analysis End!----------")          
                    break;

class  Admin:
    count=0
    def  __init__(self, un, pw):
        if  (Admin.count==0):
            self.username = un
            self.password = pw
            Admin.count = Admin.count + 1
        else:
            print ("Admin already exists")
    
    def  login(self):
        print ("Welcome to Dream Book Shop's CLI Application!")
        print ("---------------------------------------------")
        un = input ("Enter Username: ")
        pw= input ("Enter Password: ")
        if  (un == self.username and pw == self.password):
            s1 = Strategy_Selector()
            s1.OpenMenu()
        else:
            print ("Incorrect Username/Password!")
            
    
# main
a1 = Admin("David", "123098")
a1.login()










