# **Smart Travel Planner**

## **Project Overview**
Smart Travel Planner is a web application designed to help user plan their trips and exploer other users trip. Users can create,edit,and share trips, discover trips from other travelers, and leave reviews. The application aims to stream line trip planning and enhance travel expereinces for users through a simple, user friendly interface.

## **Key Features:**
- Browes and explore public trips
- Create and manage personal trips (title,destination,budget,dates, description)
- Leave reviews on public trips
- User authentication(sign up,login,logout)
- Responsive design

## **Tech Stack**
- Backend: Django,Python
- Frontend: HTML,CSS,Django Templates
- Database: SQLite (Django default database)

## **ERD**
![Image](https://github.com/user-attachments/assets/7cfb1a0c-1eec-4c74-a5a4-ca33ea09f62a)
### Description:
- Each user can create multiple trips.
- Trips can be public or private.
- Users can leave reviews on public trips.
- 

## **Installation Guide**

**Steps**
1. Clone the repository
`git clone git clone https://github.com/yourusername/smart-travel-planner.git`
`cd smart-travel-planner`

2. Createa virtual environment
 `pipenv install django`

3. Install dependencies
`pipenv shell` 

4. apply migrations
`python manage.py migrate`

5. Create superuser
`python manage.py createsuperuser`

6. Run the development server 
`python manage.py runserver`

## **User Stories**

1. **As a guest user:**

- I can browse the home page and public trips

- I can view trip details

2. **As a registered user:**

- I can create, update, and delete my trips

- I can leave reviews on public trips

- I can see only my trips in the dashboard

3. **Authentication features:**

- Sign up for a new account

- Login / Logout

- Responsive design:

- The website works well on mobile and desktop


## **Challenges and Solutions**

1. Challenge: Ensuring that only the logged-in user can modify their trips.
- Solution: Used LoginRequiredMixin and get_object_or_404 with a user=request.user filter.

2. Challenge: Handling reviews for public trips while preventing unauthorized users from posting.
- Solution: Added checks in the view to redirect guests to the home page before posting reviews.

3. Challenge: Responsive hero section and footer with minimal white space on small screens.
- Solution: Adjusted CSS padding/margin and added media queries for mobile screens.

## **Future Work**

- Add trip images upload feature

- Add highly reviewed trips to the home page

- Filter trips by budget, destination, or dates

- Add Google Maps integration for destinations
