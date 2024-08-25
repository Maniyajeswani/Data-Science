#                                                        Practo Scraper Tool
## Description:
This  streamlit application designed to scrape data(gathering total number of doctors available on practo along with their profiles) from Practo website based on user selected location and  speciality via a dropdown menu, providing an efficient tool for health industry.

## Installation instructions:
### 1.Install python 
 -	Install python in your system from python.org.
 -	During installation, make sure ADD PYTHON TO PATH option is selected.
### 2.Clone Github Repository
-	Open your terminal or command prompt
-	Navigate to the directory you want to clone the repository by using command: cd path to your directory
-	Clone the repository by using git clone command along with the github project link. For ex: git clone github_project_link
### 3. Navigate into the Project Directory
-	Now as the repository is cloned, navigate into project directory by the following command: cd repository name.
### 4.Install the required modules and libraries
-	Now when you are navigated to project directory, run the following commands in order to install the required modules and libraries:
1.pip install streamlit
2.pip install requests
3.pip install bs4
4.pip install pandas
### 5.Run the streamlit application:
-	Start the streamlit application by running: streamlit run filename.py.
                              
## Usage:
After installing, launching and accessing the web interface of the Streamlit application, follow these steps to use it effectively:
### 1.	Provide City Input:
-	Type the name of the city where you want to find doctors.
### 2.	Select Specialty:
-	Click on the dropdown and choose the appropriate specialty from 
### 3.	Scrape Data:
-	Once you’ve entered the city and selected the specialty, press the Scrape button to initiate the data scraping process.
### 4.	View Results:
-	The application will display the scraped data based on your inputs.

## Output:
After providing the city and selecting speciality from the dropdown menu , click on scrape button to begin data extraction process. The application will display the no. of doctors specializing in a particular field within specific location get displayed. Alongside this, you will able to see the detailed profiles of doctor including their name, experience, average ratings and links to their full profiles. This tool allows you to efficiently access the profiles of doctors specializing in a particular field within a particular location as listed on practo.


