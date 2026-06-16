while True:

    print("\n=== PHISHING EMAIL DETECTOR ===")
    print("1. Check Email")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        email_text = input("Paste the email message: ").lower()
        suspicious_words = ["urgent", "password", "verify", "click", "login", "bank", "refund", "winner", "prize", "account blocked", "blocked", "threat", "immediately", "account", "suspended", "security alert", "tax refund", "otp", "payment", "confirm"]
        suspicious_links = ["http://", "bit.ly", "tinyurl", "freegift", "claim"]
        score = 0
        for word in suspicious_words:
            if word in email_text:
                score += 1

        for link in suspicious_links:
            if link in email_text:
                score += 2
        
        category = "General Phishing"

        if "tax refund" in email_text or "income tax" in email_text or "gst refund" in email_text:
           category = "Tax Scam"
           

        elif "bank" in email_text or "account blocked" in email_text:
            category = "Banking Scam"
        
 
        elif "password" in email_text or "login" in email_text:
            category = "Credential Theft Attempt"
       

        print("Category:", category)

        print("Suspicious Words Found:", score)
        
        if score >= 4:
            print("Risk Level: High Risk")
            print("Result: Possible Phishing Email")
            print("Recommendation: Do not click links or share personal information.")

        elif score >= 2:
            print("Risk Level: Medium Risk")
            print("Result: Suspicious Email")
            print("Recommendation: Verify the sender before taking action.")

        else:
            print("Risk Level: Low Risk")
            print("Result: Email seems safe")
            print("Recommendation: No major threats detected.")
        report = f"""
        ---------------------
        Category: {category}
        Risk Score: {score}
        ---------------------
        """

        with open("phishing_report.txt", "a") as file:
            file.write(report)
        

        print("Report saved successfully!")

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")