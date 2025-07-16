# EMAIL_TRANSCRIBE 📧

An AI-driven automation tool that intelligently extracts contact and business details from email addresses, scrapes company websites for contextual insights, and generates hyper-personalized, visually appealing HTML emails using LLM-based content generation. The platform is designed to help businesses scale personalized outreach by combining natural language processing, web intelligence, and professional-grade email delivery.

## 🚀 Features

- **📧 Email Processing**: Upload or manually input recipient email addresses
- **🌐 Web Scraping**: Scrape company websites for additional context and insights
- **🤖 AI Content Generation**: Generate HTML email content using LLM (via Together.ai)
- **📬 Secure Email Delivery**: Send emails securely via SMTP
- **💻 User-Friendly Interface**: Lightweight and easy-to-use frontend interface
- **🎨 Customizable Templates**: Fully customizable email templates
- **📊 Business Intelligence**: Extract contact and business details automatically
- **⚡ Scalable Outreach**: Automate personalized email campaigns

## 🛠️ Technologies Used

- **Backend:** Python (Flask)
- **AI/LLM:** Together.ai API integration
- **Frontend:** HTML/CSS
- **Email Service:** SMTP
- **Web Scraping:** BeautifulSoup, Requests
- **Version Control:** Git

## 📂 Folder Structure

```
EMAIL_TRANSCRIBE/
├── app/
│   ├── static/
│   │   └── style.css                # Frontend styling
│   ├── templates/
│   │   └── index.html               # Main HTML template
│   ├── email_generator.py           # Email content generation logic
│   ├── llm_integration.py           # Together.ai LLM integration
│   ├── routes.py                    # Flask routes and endpoints
│   ├── scraper.py                   # Web scraping functionality
│   ├── smtp_mailer.py               # Email sending via SMTP
│   └── utils.py                     # Utility functions
├── env/                             # Virtual environment (included)
├── .env                             # Environment variables
├── config.py                        # Configuration settings
├── requirements.txt                 # Python dependencies
├── run.py                           # Application entry point
└── test_together_api.py             # API testing script
```

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/YujiItaori/EMAIL_TRANSCRIBE.git
cd EMAIL_TRANSCRIBE
```

> **Note:** This project includes a Python virtual environment folder (`env/`) for convenience. You may also choose to create your own.

### 2. Set Up Virtual Environment (Optional)
If you prefer to create your own virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your API keys and configuration:
```env
TOGETHER_API_KEY=your_together_ai_api_key
SMTP_SERVER=your_smtp_server
SMTP_PORT=587
SMTP_USERNAME=your_email@example.com
SMTP_PASSWORD=your_email_password
```

### 5. Run the Application
```bash
python run.py
```

Then open `http://127.0.0.1:5000/` in your browser.

## 💡 How It Works

### 1. Email Input
- Upload a list of email addresses or input them manually
- The system processes and validates email formats

### 2. Web Intelligence
- Automatically extracts company information from email domains
- Scrapes company websites for contextual business insights
- Gathers relevant data for personalization

### 3. AI Content Generation
- Uses Together.ai's LLM to generate personalized email content
- Creates contextually relevant messaging based on scraped data
- Produces professional HTML email templates

### 4. Email Delivery
- Sends personalized emails via secure SMTP
- Tracks delivery status and handles errors gracefully
- Maintains professional email formatting

## 🔧 Configuration

### SMTP Settings
Configure your email provider settings in the `.env` file:
- **Gmail**: Use `smtp.gmail.com` with port `587`
- **Outlook**: Use `smtp-mail.outlook.com` with port `587`
- **Custom SMTP**: Configure according to your provider's specifications

### API Configuration
- Sign up for a Together.ai account and obtain your API key
- Add the API key to your `.env` file
- Test the API connection using `test_together_api.py`

## 📊 Usage Examples

### Basic Email Campaign
1. Navigate to the web interface
2. Upload your email list or input addresses manually
3. Configure email templates and personalization settings
4. Review generated content and send emails

### Advanced Personalization
- The system automatically researches each recipient's company
- Generates unique, contextually relevant email content
- Adapts messaging based on industry and company insights

## 🛡️ Security Features

- **Secure SMTP**: All emails sent through encrypted connections
- **API Security**: Together.ai API keys stored securely in environment variables
- **Input Validation**: Email addresses and inputs are validated and sanitized
- **Error Handling**: Comprehensive error handling for failed deliveries

## 📋 Requirements

- Python 3.7+
- Together.ai API key
- SMTP email account
- Internet connection for web scraping

## 🧩 Troubleshooting

### Common Issues:

**❌ API Connection Error**
→ Verify your Together.ai API key in the `.env` file

**❌ SMTP Authentication Failed**
→ Check your email credentials and enable "Less secure app access" if using Gmail

**❌ Web Scraping Blocked**
→ Some websites may block automated requests; the system handles these gracefully

**❌ Email Not Delivered**
→ Check spam folders and verify recipient email addresses

## 🔄 Future Enhancements

- **Email Analytics**: Track open rates and click-through rates
- **Template Library**: Pre-built email templates for different industries
- **CRM Integration**: Connect with popular CRM systems
- **Scheduling**: Schedule email campaigns for optimal delivery times
- **A/B Testing**: Test different email variations automatically

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 👨‍💻 Author

**Yuji Itaori**  
GitHub Profile → https://github.com/YujiItaori

---

⭐ **Star this repository if you find it helpful!** ⭐



![Screenshot 2025-06-13 085940](https://github.com/user-attachments/assets/50e3dedc-2201-419d-8b33-dd09d79c9a78)
![Screenshot 2025-06-13 090004](https://github.com/user-attachments/assets/cb55da37-ea20-47a8-bbc9-dee73cbe5ec1)
![Screenshot 2025-06-13 090012](https://github.com/user-attachments/assets/f1870dec-95f7-4937-b7bf-5cd01b410eb8)

