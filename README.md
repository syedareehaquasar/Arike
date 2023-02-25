
Introducing Arike
"Arike" is a project that aims to improve the palliative care system for patients who need constant or specialized medical attention. The word "Arike" comes from Malayalam and translates to "Alongside" or "Besides" in English.

In India, palliative care is provided by a team of specialized nurses who visit patients under their Panchayat/Municipality/Corporation to relieve their suffering and provide them with the best possible quality of life. However, the current system is paper-based, making it inefficient and prone to errors.

Our capstone project is to build a system that automates and streamlines the palliative care process, making it more efficient and accurate.

Basics of Arike
In palliative care, there are "Primary Health Centers" (PHC) and "Community Health Centers" (CHC) that reside in a ward belonging to one of the many LSGs (Local Self-Government) in a district. Primary nurses visit patients locality-wise every month, go through their case sheets, and provide them with the care they need. If a patient needs expert care, they are referred to a specialist nurse from the CHC.

The main users of Arike are:

Primary Nurse: responsible for maintaining all health records for a patient under their PHC.

Secondary Nurse: specialist nurses from the CHC who provide special care for a patient when referred by a primary nurse.

District Admin: responsible for accessing records under the user's district. This user has full access to the data and can create and delete Primary or Secondary nurses.

Main Entities
Facility: can be a PHC or CHC.
Patient: registered in a PHC and referred to a CHC. They are the object whose data we deal with in the system.
<!--### Expected Wireframe:
https://www.figma.com/file/kgOXmtptNxJUvkJ2qjeyzA/Django-201-Capstone?node-id=3%3A1146-->
Login Details:
You can log in to the system using the following credentials:

makefile
Copy code
Username: distadmin 
Password: distadmin
UserType: District Admin

Username: primarynurse
Password: primarynurse
UserType: Primary Nurse

Username: secondarynurse
Password: secondarynurse
UserType: Secondary Nurse
