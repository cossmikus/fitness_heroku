Management Application

- **Website:**  https://frontend-fitness.vercel.app/
Бэкенд для приложения по управлению расписанием фитнес-тренеров

This application facilitates user registration, authentication, and schedule management, deployed with a backend on Heroku and a frontend on Vercel.

## Backend

### Overview

The backend is developed with Django and handles user authentication, schedule management, and more, using JWT for secure access.

- **Deployed Backend**: [https://fitnessheroku-2b7e0fea23b9.herokuapp.com/](https://fitnessheroku-2b7e0fea23b9.herokuapp.com/)
- **Backend repository**: [https://github.com/cossmikus/fitness_heroku](https://github.com/cossmikus/fitness_heroku)


- **Deployed Frontend**: [https://frontend-fitness.vercel.app/](https://frontend-fitness.vercel.app/)
- **Frontend repository**: [https://github.com/cossmikus/frontend_fitness](https://github.com/cossmikus/frontend_fitness)

### Features

- User registration and login with JWT authentication.
- CRUD operations for user and schedule management.
- PostgreSQL database.

### API Endpoints

```plaintext
- GET / - Retrieves all users
- GET /<int:pk>/ - Retrieves a user by ID
- POST /register - Registers a new user
- PUT /update/<int:pk> - Updates a user by ID
- DELETE /delete/<int:pk> - Deletes a user by ID
- GET /admin - Retrieves admin information
- GET /trainer - Retrieves trainer information
- GET /client - Retrieves client information
- POST /login - Authenticates a user
- GET /getTrainerInfo - Retrieves trainer names
- GET /getClientsInfo - Retrieves clients info
- GET /getScheduleTrainer/<int:pk> - Retrieves a trainer's schedule
- GET /getAllSchedules - Retrieves all schedules
- GET /getScheduleClient/<int:pk> - Retrieves a client's schedule
- POST /addSchedule - Adds a new schedule
