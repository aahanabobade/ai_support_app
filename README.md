### AI-Powered Customer Support Interface
---
A simple AI-powered customer support system where support agents can view customer queries, respond manually, or auto-generate AI responses. Customers can create tickets, view their status, and communicate with support efficiently.

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
4. Configure Environment Variables

Create a .env file in the root directory with:
  
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

5. Set Gemini API Key
```bash
# macOS/Linux
export GEMINI_API_KEY='your_gemini_api_key_here'

# Windows (PowerShell)
setx GEMINI_API_KEY "your_gemini_api_key_here"
```
6. Run Database Management system
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Run the server
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
6. No real-time updates; AI response generation is synchronous
7. No file attachments for tickets
8. AI classification may sometimes default to General if uncertain.
9. Currently tested with small datasets and single server deployment

### Usage
1. Customer: Register → Login → Create ticket → View ticket status → Chat with support
2. Admin: Login → View all tickets → Generate/Regenerate AI response → Update ticket status

### Requirements
All dependencies are included in requirements.txt. Install them via:
```bash
pip install -r requirements.txt
```

### Tech Stack

1. Single Machine Testing: The system is tested locally; production deployment may require Docker, a web server, and proper environment variable management.
2. AI Reliability: AI responses might occasionally require manual correction.
3. No Multi-language Support: Currently supports only English.
4. Basic UI/UX: Focus is on functionality rather than advanced design.
5. Admin Panel Role Check: Admin cannot act as customer, but the interface is basic and could be enhanced with detailed role validation messages.

### Future Improvements
1. Real-time notifications for ticket updates
2. File attachments and rich text support for tickets
3. Multi-language support for AI responses

### Contact/Support
This project is maintained by Aahana Bobade. For any issues or questions regarding setup or usage, please contact via GitHub or email(aahanabobade@gmail.com).
