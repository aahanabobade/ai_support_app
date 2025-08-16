### AI-Powered Customer Support Interface
---
EduvanceAI is a simple AI-powered customer support interface that allows support agents to view customer queries, respond manually, or auto-generate AI-powered responses. It provides role-based login for customers and admins, ticket creation and tracking, and AI-assisted classification and response.

---
### Features 
1. Role-based Login: Separate login for Customers and Admins.
2. Customer Tickets: Customers can create new tickets and view ticket history.
3. Admin Panel: Admins can view all tickets, reply manually, or generate AI responses.
4. AI-Powered Ticket Classification: Automatically classifies tickets into Billing, Technical, or General.
5. AI-Powered Responses: Admins can auto-generate professional responses using Google Gemini AI.
6. Re-generate Responses: Admins can regenerate AI responses if the first response isn’t satisfactory.
7. Registration: New customers can register directly via a simple registration form.
8. Security: Role validation prevents admins from logging in as customers or vice versa. CSRF protection and authentication are included.
---
### Setup Instruction
1. Clone the Repository
```bash
git clone https://github.com/aahanabobade/ai_support_app.git
cd ai_support_app
```
2. Create and Activate Virtual Environment
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
If requirements.txt does not exist, generate it using:
```bash
pip freeze > requirements.txt
```
4. Set Gemini API Key
```bash
# macOS/Linux
export GEMINI_API_KEY='your_gemini_api_key_here'

# Windows (PowerShell)
setx GEMINI_API_KEY "your_gemini_api_key_here"
```
5. Run Database Management system
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Run the server
```bash
python manage.py runserver
```
Open your browser and visit: http://127.0.0.1:8000/

### Assumptions

1. User Roles: Customers and Admins are clearly separated; admin accounts are created in Django admin.
2. AI Responses: Google Gemini AI is used to generate responses; accuracy depends on the AI model.
3. Security: CSRF protection and user authentication are enforced.
4. Environment Variables: Gemini API key must be exported locally before running the server.
5. No Real-time Notifications: The system is not integrated with SMS/email alerts for ticket updates.

### Limitations

1. Single Machine Testing: The system is tested locally; production deployment may require Docker, a web server, and proper environment variable management.
2. AI Reliability: AI responses might occasionally require manual correction.
3. No Multi-language Support: Currently supports only English.
4. Basic UI/UX: Focus is on functionality rather than advanced design.
5. Admin Panel Role Check: Admin cannot act as customer, but the interface is basic and could be enhanced with detailed role validation messages.

### Tech Stack

1. Single Machine Testing: The system is tested locally; production deployment may require Docker, a web server, and proper environment variable management.
2. AI Reliability: AI responses might occasionally require manual correction.
3. No Multi-language Support: Currently supports only English.
4. Basic UI/UX: Focus is on functionality rather than advanced design.
5. Admin Panel Role Check: Admin cannot act as customer, but the interface is basic and could be enhanced with detailed role validation messages.

### How to use

1. Register as a new customer or log in as an existing one.
2. Customers can create tickets with messages describing their issues.
3. Admins can:
    a. View all tickets.
    b. Manually respond to tickets
    c. Auto-generate responses via AI
    d. Re-generate AI responses if needed
4. Customers can view replies and ticket status.

### Contact/Support
This project is maintained by Aahana Bobade. For any issues or questions regarding setup or usage, please contact via GitHub or email(aahanabobade@gmail.com).
