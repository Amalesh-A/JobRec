import pandas as pd
import gradio as gr
#import openai
currentpage = 1
jobdata = pd.read_csv("us-software-engineer-jobs-updated-links-replaced.csv")

def recommend_jobs(title=None, location=None, remote_work=None, urgently_hiring=None, sponsored=None, page=1, results_per_page=5):
    filtered_jobs = jobdata
    
    # Filter by job title if provided
    if title:
        filtered_jobs = filtered_jobs[filtered_jobs['title'].str.contains(title, case=False, na=False)]
    
    # Filter by location if provided
    if location:
        filtered_jobs = filtered_jobs[filtered_jobs['location'].str.contains(location, case=False, na=False)]
    
    # Filter by remote work model if provided
    if remote_work:
        filtered_jobs = filtered_jobs[filtered_jobs['remote_work_model'].str.contains(remote_work, case=False, na=False)]
    
    # Filter by urgently hiring if provided
    if urgently_hiring:
        filtered_jobs = filtered_jobs[filtered_jobs['urgently_hiring'].str.contains(urgently_hiring, case=False, na=False)]

    if sponsored:
        filtered_jobs = filtered_jobs[filtered_jobs['sponsored'].str.strip().str.lower().str.contains(sponsored.strip().lower(), case=False, na=False)]
    
    # Select relevant columns for display
    display_columns = ['title', 'company', 'location', 'types', 'remote_work_model', 'urgently_hiring', 'sponsored', 'link']
    #result = filtered_jobs[display_columns]  # Show top 5 results
    
    # If no matching jobs are found
    '''if result.empty:
        return "No matching jobs found. Try different criteria."
    else:
        return result.to_string(index=False)'''
    #if result.empty:
     #   return pd.DataFrame(columns=display_columns)
     # Pagination logic
    start_index = (page - 1) * results_per_page
    end_index = start_index + results_per_page
    
    # Paginate results
    result = filtered_jobs[display_columns].iloc[start_index:end_index]
    return result
    
def chatbot(title, location, remote_work, urgently_hiring, sponsored, page = 1, results_per_page=5):
    '''prompt = f"Recommend jobs based on the following criteria:\nJob title: {title}\nLocation: {location}\nRemote work: {remote_work}\nUrgently hiring: {urgently_hiring}\nVisa Sponsorship: {sponsored}"
    # Call OpenAI API for generating a conversational response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens = 50
    )
    
    # Extract the AI's response text
    ai_response = response.choices[0]['message']['content'].strip()
    
    # Get job recommendations based on filters
    job_recommendations = recommend_jobs(title=title, location=location, remote_work=remote_work, urgently_hiring=urgently_hiring, sponsored=sponsored)
    
    # Return both AI response and job recommendations
    return ai_response, job_recommendations'''

    global currentpage

    # Custom AI response generated from the dataset, removing OpenAI call
    response = f"Based on the criteria you provided, here are some job recommendations for a {title} role:\n\n"
    
    # Get job recommendations based on filters
    job_recommendations = recommend_jobs(title=title, location=location, remote_work=remote_work, urgently_hiring=urgently_hiring, sponsored=sponsored, page=currentpage, results_per_page=results_per_page)
    
    if not job_recommendations.empty:
        # Loop through the filtered job recommendations and add them to the response
        for index, row in job_recommendations.iterrows():
            response += f"   Company: {row['company']}\n"
            response += f"   Job Title: {row['title']}\n"
            response += f"   Location: {row['location']}\n"
            response += f"   Urgently Hiring: {row['urgently_hiring']}\n"
            response += f"   Visa Sponsorship: {row['sponsored']}\n\n"

        if len(jobdata) > currentpage * results_per_page:
            response += f"\nShowing {results_per_page} results per page. Click 'Next' to view more results."
    else:
        response += "No matching jobs found for your criteria."
    
    # Return the formatted response and the job recommendations as a dataframe
    return response
#, job_recommendations

def next_page(title, location, remote_work, urgently_hiring, sponsored):
    global currentpage
    currentpage += 1  # Increment the current page number
    return chatbot(title, location, remote_work, urgently_hiring, sponsored)


'''demo = gr.Interface(
    fn=chatbot,
    inputs=[
        gr.Textbox(placeholder="Enter job title (for example, Engineer, Developer)", label="Preferred Job Title"),
        gr.Textbox(placeholder="Enter location - City, State (for example, Remote, California)", label="Preferred Location"),
        gr.Textbox(placeholder="Enter your Work Preference ('100% Remote', 'No Remote', 'Hybrid', or Leave Empty)", label="Preferred Work Model"),
        gr.Textbox(placeholder="Is the company hiring urgently? ('Yes', 'No', or Leave Empty)", label="Urgently hiring"),
        gr.Textbox(placeholder="Do you need Visa Sponsorship?('Yes', 'No')", label="Visa Sponsorship")
    ],
    outputs=gr.Textbox(label="AI Response"), 
    title="Job Recommendation Chatbot",
    description="Get job recommendations based on job title, location, remote work preference, and urgency."
)
'''
# Gradio interface with a 'Next' button
with gr.Blocks() as demo:
    title_input = gr.Textbox(placeholder="Enter job title (for example, Engineer, Developer)", label="Preferred Job Title")
    location_input = gr.Textbox(placeholder="Enter location (for example, Remote, California)", label="Preferred Location")
    work_model_input = gr.Textbox(placeholder="Enter your Work Preference ('100% Remote', 'No Remote', 'Hybrid', or Leave Empty)", label="Preferred Work Model")
    urgent_input = gr.Textbox(placeholder="Is the company hiring urgently? ('Yes', 'No', or Leave Empty)", label="Urgently hiring")
    sponsorship_input = gr.Textbox(placeholder="Do you need Visa Sponsorship?('Yes', 'No')", label="Visa Sponsorship")
    
    output_box = gr.Textbox(label="AI Response")

    # First interaction
    recommend_button = gr.Button("Get Recommendations")
    recommend_button.click(chatbot, [title_input, location_input, work_model_input, urgent_input, sponsorship_input], output_box)

    # Next page interaction
    next_button = gr.Button("Next")
    next_button.click(next_page, [title_input, location_input, work_model_input, urgent_input, sponsorship_input], output_box)


# Step 4: Launch the chatbot
demo.launch()