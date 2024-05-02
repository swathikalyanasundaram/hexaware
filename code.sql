create database careerhub;
use careerhub;

CREATE TABLE Companies (
    CompanyID INT PRIMARY KEY,
    CompanyName VARCHAR(255),
    Location VARCHAR(255)
);
CREATE TABLE Jobs (
    JobID INT PRIMARY KEY,
    CompanyID INT,
    JobTitle VARCHAR(255),
    JobDescription TEXT,
    JobLocation VARCHAR(255),
    Salary DECIMAL(10, 2),
    JobType VARCHAR(50),
    PostedDate DATETIME,
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID)
);
CREATE TABLE Applicants (
	applicantid INT PRIMARY KEY,
	firstname VARCHAR(25),
	lastname VARCHAR(25),
	email varchar(255),
	phone varchar(20),
	resume TEXT,
	city varchar(255),
	state varchar(255)
);
CREATE TABLE Applications (
    ApplicationID INT PRIMARY KEY,
    JobID INT,
    ApplicantID INT,
    ApplicationDate DATETIME,
    CoverLetter TEXT,
    FOREIGN KEY (JobID) REFERENCES Jobs(JobID),
    FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID)
);

INSERT INTO Companies (CompanyID,CompanyName, Location) VALUES
(1,'Tech Innovations', 'San Francisco'),
(2,'Data Driven Inc', 'New York'),
(3,'GreenTech Solutions', 'Austin'),
(4,'CodeCrafters', 'Boston'),
(5,'HexaWare Technologies', 'Chennai');


INSERT INTO Jobs (JobID,CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate) VALUES
(1,1, 'Frontend Developer', 'Develop user-facing features', 'San Francisco', 75000, 'Full-time', '2023-01-10'),
(2,2, 'Data Analyst', 'Interpret data models', 'New York', 68000, 'Full-time', '2023-02-20'),
(3,3, 'Environmental Engineer', 'Develop environmental solutions', 'Austin', 85000, 'Full-time', '2023-03-15'),
(4,1, 'Backend Developer', 'Handle server-side logic', 'Remote', 77000, 'Full-time', '2023-04-05'),
(5,4, 'Software Engineer', 'Develop and test software systems', 'Boston', 90000, 'Full-time', '2023-01-18'),
(6,5, 'HR Coordinator', 'Manage hiring processes', 'Chennai', 45000, 'Contract', '2023-04-25'),
(7,2, 'Senior Data Analyst', 'Lead data strategies', 'New York', 95000, 'Full-time', '2023-01-22');


INSERT INTO Applicants (applicantid,FirstName, LastName, Email, Phone, Resume,city,state) VALUES
(1,'John', 'Doe', 'john.doe@example.com', '123-456-7890', 'Experienced web developer with 5 years of experience.','chennai','tamil nadu'),
(2,'Jane', 'Smith', 'jane.smith@example.com', '234-567-8901', 'Data enthusiast with 3 years of experience in data analysis.','madurai','tamil nadu'),
(3,'Alice', 'Johnson', 'alice.johnson@example.com', '345-678-9012', 'Environmental engineer with 4 years of field experience.','bengaluru','karnataka'),
(4,'Bob', 'Brown', 'bob.brown@example.com', '456-789-0123', 'Seasoned software engineer with 8 years of experience.','varkala','kerala');


INSERT INTO Applications (ApplicationID,JobID, ApplicantID, ApplicationDate, CoverLetter) VALUES
(1,1, 1, '2023-04-01', 'I am excited to apply for the Frontend Developer position.'),
(2,2, 2, '2023-04-02', 'I am interested in the Data Analyst position.'),
(3,3, 3, '2023-04-03', 'I am eager to bring my expertise to your team as an Environmental Engineer.'),
(4,4, 4, '2023-04-04', 'I am applying for the Backend Developer role to leverage my skills.'),
(5,5, 1, '2023-04-05', 'I am also interested in the Software Engineer position at CodeCrafters.');

select * from Companies;

select * from Jobs;

select*from Applicants;

select*from Applications;

--5. Write an SQL query to count the number of applications received for each job listing in the
--"Jobs" table. Display the job title and the corresponding application count. Ensure that it lists alljobs, even if they have no applications.


select j.JobId,j.JobTitle,count(a.ApplicationID) from Jobs j
left join Applications a on j.JobID=a.JobID
group by j.JobID,j.JobTitle


--6.Develop an SQL query that retrieves job listings from the "Jobs" table within a specified salary
--range. Allow parameters for the minimum and maximum salary values. Display the job title,company name, location, and salary for each matching job

DECLARE @MinSalary DECIMAL(10, 2);
DECLARE @MaxSalary DECIMAL(10, 2);

SELECT 
    @MinSalary = MIN(Salary),
    @MaxSalary = MAX(Salary)
FROM 
    Jobs;

select j.JobTitle,c.CompanyName,c.location,j.salary from Jobs j
inner join Companies c on j.CompanyID = c.CompanyID
where j.Salary BETWEEN @MinSalary AND @MaxSalary;

--7.Write an SQL query that retrieves the job application history for a specific applicant. Allow a
--parameter for the ApplicantID, and return a result set with the job titles, company names, and application dates for all the jobs the applicant has applied to.

declare @applicantid int = 1;
select j.jobtitle,c.companyname,a.applicationdate from Applications a
inner join jobs j on j.JobID=a.JobID
inner join Companies c on j.CompanyID=c.CompanyID
where a.ApplicantID= @applicantid

--8.Create an SQL query that calculates and displays the average salary offered by all companies for
--job listings in the "Jobs" table. Ensure that the query filters out jobs with a salary of zero.

select c.companyname,avg(j.salary) as avg from jobs j 
inner join Companies c on j.CompanyID=c.CompanyID
where j.Salary > 0
group by c.CompanyName;

--9.Write an SQL query to identify the company that has posted the most job listings. Display the
--company name along with the count of job listings they have posted. Handle ties if multiple
--companies have the same maximum count.

select c.companyname,count(j.companyid) as count from jobs j
inner join Companies c on c.CompanyID=j.CompanyID
group by c.CompanyName 
order by count desc 
offset 0 rows fetch next 1 rows only;

--10.Find the applicants who have applied for positions in companies located in 'new york' and have at
--least 3 years of experience.

select * from Applicants a
inner join Applications app on a.applicantid=app.ApplicantID
inner join jobs j on app.JobID=j.JobID
where j.joblocation='new york' and  a.resume like '%3%' 

--11.Retrieve a list of distinct job titles with salaries between $60,000 and $80,000.

select distinct jobtitle,salary from jobs
where Salary between 60000 and 80000;

--12.Find the jobs that have not received any applications.
select j.*from jobs j
left join Applications a on j.JobID=a.JobID
where a.ApplicationID is null

--13.Retrieve a list of job applicants along with the companies they have applied to and the positions
--they have applied for.

select a.applicantid,j.jobid,j.jobtitle from Applications a
left join jobs j on j.JobID=a.JobID

--14.Retrieve a list of companies along with the count of jobs they have posted, even if they have not
--received any applications.
select c.companyname,count(j.jobid)as count from Companies c
left join jobs j on j.CompanyID=c.CompanyID
group by c.CompanyName

--15.List all applicants along with the companies and positions they have applied for, including those
--who have not applied.

SELECT a.FirstName, a.LastName, c.CompanyName, j.JobTitle
FROM Applicants a
CROSS JOIN Companies c
LEFT JOIN ( SELECT ap.ApplicantID, j.JobID, j.CompanyID, j.JobTitle
    FROM Applications ap
    JOIN Jobs j ON ap.JobID = j.JobID) AS ApplicantJobs ON a.ApplicantID = ApplicantJobs.ApplicantID AND c.CompanyID = ApplicantJobs.CompanyID
LEFT JOIN Jobs j ON ApplicantJobs.JobID = j.JobID;

--16. . Find companies that have posted jobs with a salary higher than the average salary of all jobs.

SELECT  DISTINCT c.CompanyName
FROM  Companies c
JOIN Jobs j ON c.CompanyID = j.CompanyID
WHERE j.Salary > (SELECT AVG(Salary) FROM Jobs);

--17.  Display a list of applicants with their names and a concatenated string of their city and state.

select firstname,lastname,concat(city,',',state) as location
from Applicants;

--18. Retrieve a list of jobs with titles containing either 'Developer' or 'Engineer'
select * from jobs
where jobtitle like '%developer' or jobtitle like '%engineer';

--19.Retrieve a list of applicants and the jobs they have applied for, including those who have not
--applied and jobs without applicants.
SELECT a.FirstName, a.LastName, j.JobTitle
FROM Applicants a
CROSS JOIN Jobs j
LEFT JOIN Applications app ON a.ApplicantID = app.ApplicantID AND j.JobID = app.JobID;

--20.List all combinations of applicants and companies where the company is in a specific city and the
--applicant has more than 2 years of experience. For example: city=Chennai

select a.firstname,a.lastname,c.companyname from Applicants a
cross join companies c
left join Applications app on a.applicantid=app.ApplicantID
left join jobs j on app.JobID=j.JobID
where c.Location = 'chennai'and a.resume like '%3%' or a.resume like '%4%';
