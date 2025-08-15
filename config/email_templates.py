import os
from typing import Dict, Any

class EmailTemplateConfig:
    """Configuration for Supabase email templates"""
    
    def __init__(self):
        self.frontend_url = os.getenv('FRONTEND_URL', 'http://localhost:3000')
        self.app_name = os.getenv('APP_NAME', 'MechAgent')
        self.support_email = os.getenv('SUPPORT_EMAIL', 'support@mechagent.com')
    
    def get_password_reset_template(self) -> Dict[str, Any]:
        """Get password reset email template configuration"""
        return {
            'subject': f'Reset your {self.app_name} password',
            'template': self._get_password_reset_html(),
            'redirect_to': f'{self.frontend_url}/auth/reset-password'
        }
    
    def get_email_confirmation_template(self) -> Dict[str, Any]:
        """Get email confirmation template configuration"""
        return {
            'subject': f'Confirm your {self.app_name} email',
            'template': self._get_email_confirmation_html(),
            'redirect_to': f'{self.frontend_url}/auth/login'
        }
    
    def _get_password_reset_html(self) -> str:
        """HTML template for password reset email"""
        return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reset Your Password</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f8f9fa;
        }}
        .container {{
            background-color: #ffffff;
            border-radius: 8px;
            padding: 40px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .logo {{
            font-size: 24px;
            font-weight: bold;
            color: #2563eb;
            margin-bottom: 10px;
        }}
        .title {{
            font-size: 28px;
            font-weight: bold;
            color: #1f2937;
            margin-bottom: 10px;
        }}
        .subtitle {{
            font-size: 16px;
            color: #6b7280;
            margin-bottom: 30px;
        }}
        .button {{
            display: inline-block;
            background-color: #2563eb;
            color: #ffffff;
            text-decoration: none;
            padding: 14px 28px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 16px;
            margin: 20px 0;
            text-align: center;
        }}
        .button:hover {{
            background-color: #1d4ed8;
        }}
        .info-box {{
            background-color: #f3f4f6;
            border-left: 4px solid #2563eb;
            padding: 16px;
            margin: 20px 0;
            border-radius: 4px;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e5e7eb;
            font-size: 14px;
            color: #6b7280;
        }}
        .security-note {{
            background-color: #fef3c7;
            border: 1px solid #f59e0b;
            border-radius: 4px;
            padding: 12px;
            margin: 20px 0;
            font-size: 14px;
            color: #92400e;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">{self.app_name}</div>
            <h1 class="title">Reset Your Password</h1>
            <p class="subtitle">We received a request to reset your password</p>
        </div>
        
        <div class="content">
            <p>Hello,</p>
            <p>You recently requested to reset your password for your {self.app_name} account. Click the button below to reset it:</p>
            
            <div style="text-align: center;">
                <a href="{{{{ .ConfirmationURL }}}}" class="button">Reset Password</a>
            </div>
            
            <div class="info-box">
                <strong>Important:</strong> This password reset link will expire in 24 hours for security reasons.
            </div>
            
            <div class="security-note">
                <strong>Security Notice:</strong> If you didn't request this password reset, please ignore this email. Your password will remain unchanged.
            </div>
            
            <p>If the button above doesn't work, you can copy and paste the following link into your browser:</p>
            <p style="word-break: break-all; color: #2563eb;">{{{{ .ConfirmationURL }}}}</p>
        </div>
        
        <div class="footer">
            <p>This email was sent by {self.app_name}</p>
            <p>If you have any questions, contact us at <a href="mailto:{self.support_email}">{self.support_email}</a></p>
        </div>
    </div>
</body>
</html>
        """.strip()
    
    def _get_email_confirmation_html(self) -> str:
        """HTML template for email confirmation"""
        return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Confirm Your Email</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f8f9fa;
        }}
        .container {{
            background-color: #ffffff;
            border-radius: 8px;
            padding: 40px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .logo {{
            font-size: 24px;
            font-weight: bold;
            color: #2563eb;
            margin-bottom: 10px;
        }}
        .title {{
            font-size: 28px;
            font-weight: bold;
            color: #1f2937;
            margin-bottom: 10px;
        }}
        .subtitle {{
            font-size: 16px;
            color: #6b7280;
            margin-bottom: 30px;
        }}
        .button {{
            display: inline-block;
            background-color: #10b981;
            color: #ffffff;
            text-decoration: none;
            padding: 14px 28px;
            border-radius: 6px;
            font-weight: 600;
            font-size: 16px;
            margin: 20px 0;
            text-align: center;
        }}
        .button:hover {{
            background-color: #059669;
        }}
        .info-box {{
            background-color: #f3f4f6;
            border-left: 4px solid #10b981;
            padding: 16px;
            margin: 20px 0;
            border-radius: 4px;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e5e7eb;
            font-size: 14px;
            color: #6b7280;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">{self.app_name}</div>
            <h1 class="title">Welcome to {self.app_name}!</h1>
            <p class="subtitle">Please confirm your email address</p>
        </div>
        
        <div class="content">
            <p>Hello,</p>
            <p>Thank you for signing up for {self.app_name}! To complete your registration, please confirm your email address by clicking the button below:</p>
            
            <div style="text-align: center;">
                <a href="{{{{ .ConfirmationURL }}}}" class="button">Confirm Email</a>
            </div>
            
            <div class="info-box">
                <strong>Next Steps:</strong> After confirming your email, you'll be able to sign in and start using {self.app_name}.
            </div>
            
            <p>If the button above doesn't work, you can copy and paste the following link into your browser:</p>
            <p style="word-break: break-all; color: #10b981;">{{{{ .ConfirmationURL }}}}</p>
        </div>
        
        <div class="footer">
            <p>This email was sent by {self.app_name}</p>
            <p>If you have any questions, contact us at <a href="mailto:{self.support_email}">{self.support_email}</a></p>
        </div>
    </div>
</body>
</html>
        """.strip()

# Create instance for easy import
email_config = EmailTemplateConfig()