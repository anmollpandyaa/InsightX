# InsightX: Automated Research and Trigger Finder (ART Finder)

## Overview
InsightX is a cutting-edge solution designed to streamline the research phase of ad creation. By leveraging AI-driven models, InsightX automates data gathering and generates actionable insights, empowering startups and marketers to craft compelling campaigns.

---

## Features
1. **Comprehensive Research Automation**:  
   - Scrapes data from blogs, forums, social media, app reviews, and YouTube videos.  
   - Analyzes competitor ads to identify trends, pain points, and effective solutions.

2. **Actionable Insights Generation**:  
   - Summarizes triggers, user problems, and solutions tailored to specific audiences.  
   - Recommends high-performing hooks and CTAs for the target market.

3. **Secure and Structured Data Storage**:  
   - Stores summaries and insights in a structured database for easy access and sharing.  

4. **Short and Concise Summaries**:  
   - Outputs clear and actionable summaries of insights for effective decision-making.

---

## Technology Stack

### 1. **Backend**:
- **Programming Language**: Java  
- **Framework**: Spring Boot  
  - RESTful APIs for handling keyword input and serving insights.  
  - Handles requests between the UI, Langflow, and the database.  

### 2. **AI Model**:  
- **Large Language Models (LLMs)**:  
   - Used for trend analysis, user point-of-view extraction, insights generation, and summarization.  
   - Processes input keywords and generates actionable insights via Langflow.  

### 3. **Flow Management**:
- **Langflow**:  
   - Orchestrates input handling, invokes the AI model, and manages workflows.

### 4. **Storage**:
- **Astradb**:  
   - Stores summaries and insights securely for quick retrieval and sharing.

### 5. **User Interface (UI)**:
- **Frontend Stack**:  
  - **HTML/CSS**: Designed using Materialize for a modern, responsive look.  
  - **JavaScript**: Manages client-side logic for interacting with the backend API.  
- **Features**:  
  - Input field for entering keywords.  
  - Display section for summarizing results.  
  - Designed to integrate seamlessly with the backend APIs.

---

## Workflow
1. **User Input**:
   - The user enters a keyword in the UI input field.  

2. **Processing**:
   - The keyword is sent to the Spring Boot backend via a RESTful API.  
   - Langflow orchestrates the flow by sending the input to an LLM model for insights generation.  

3. **Insights Generation**:
   - The LLM processes data, identifies trends, and creates a concise summary.  
   - Results are stored in Astradb for easy access and sharing.

4. **Output Display**:
   - The backend retrieves stored results and sends them to the UI.  
   - The UI displays insights in a user-friendly format, including suggested hooks, CTAs, and areas of focus.

---

## Key Highlights
- **AI-Powered Insights**: Automated trend and insight generation through advanced LLMs.
- **Secure Storage**: Leveraging Astradb for secure, scalable data storage.
- **Seamless Flow Management**: Langflow simplifies model integration and task orchestration.
- **User-Friendly Interface**: Responsive UI built with Materialize CSS and JavaScript.

---

## Future Enhancements
1. **Enhanced UI**:  
   - Add a dashboard for historical insights and keyword performance metrics.  

2. **Advanced Analytics**:  
   - Integrate visualization tools like charts and graphs for a deeper understanding of trends.  

3. **Multi-Model Support**:  
   - Extend support for multiple AI models for comparative analysis.

4. **User Authentication**:  
   - Implement user roles and authentication for access control.

5. **Real-Time Analysis**:  
   - Enable real-time data scraping and insight generation for dynamic topics.

---

## How It Works
```text
Input (Keyword) -> REST API (Spring Boot) -> Langflow (LLM Workflow) -> AI Model -> Insights Summary -> Store in Astradb -> Display on UI
