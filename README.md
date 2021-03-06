![Django CI](https://github.com/pontushed/hy-cybersecurity-project/workflows/Django%20CI/badge.svg)

# Cybersecurity Base 2020 Project

Pontus Hedlund

## Present Application Security Risks

1. [**Injection**](/www-project-top-ten/2017/A1_2017-Injection). Injection flaws, such as SQL, NoSQL, OS, and LDAP injection, occur when untrusted data is sent to an interpreter as part of a command or query. The attacker's hostile data can trick the interpreter into executing unintended commands or accessing data without proper authorization.
2. [**Broken Authentication**](/www-project-top-ten/2017/A2_2017-Broken_Authentication). Application functions related to authentication and session management are often implemented incorrectly, allowing attackers to compromise passwords, keys, or session tokens, or to exploit other implementation flaws to assume other users' identities temporarily or permanently.
3. [**Sensitive Data Exposure**](/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure). Many web applications and APIs do not properly protect sensitive data, such as financial, healthcare, and PII. Attackers may steal or modify such weakly protected data to conduct credit card fraud, identity theft, or other crimes. Sensitive data may be compromised without extra protection, such as encryption at rest or in transit, and requires special precautions when exchanged with the browser.
4. [**Broken Access Control**](/www-project-top-ten/2017/A5_2017-Broken_Access_Control). Restrictions on what authenticated users are allowed to do are often not properly enforced. Attackers can exploit these flaws to access unauthorized functionality and/or data, such as access other users' accounts, view sensitive files, modify other users' data, change access rights, etc.
5. [**Cross-Site Scripting XSS**](</www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS)>). XSS flaws occur whenever an application includes untrusted data in a new web page without proper validation or escaping, or updates an existing web page with user-supplied data using a browser API that can create HTML or JavaScript. XSS allows attackers to execute scripts in the victim's browser which can hijack user sessions, deface web sites, or redirect the user to malicious sites.
6. [**Insufficient Logging & Monitoring**](/www-project-top-ten/2017/A10_2017-Insufficient_Logging%2526Monitoring). Insufficient logging and monitoring, coupled with missing or ineffective integration with incident response, allows attackers to further attack systems, maintain persistence, pivot to more systems, and tamper, extract, or destroy data. Most breach studies show time to detect a breach is over 200 days, typically detected by external parties rather than internal processes or monitoring.
