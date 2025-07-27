import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Generative BI: Theory & Implementation", page_icon="📊", layout="wide")

# Custom CSS for better presentation
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2rem;
        color: #2ca02c;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .code-explanation {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .pros-cons-box {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .pros-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .cons-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
    .comparison-box {
        padding: 1rem;
        border-radius: 0.5rem;
        color: #333;
    }
    .traditional-bi-box {
        background-color: #e8f4fd;
        border: 1px solid #bee5eb;
    }
    .generative-bi-box {
        background-color: #e8fde8;
        border: 1px solid #c3e6c3;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to:", 
    ["🏠 Introduction", 
     "📚 Theory: What is Generative BI?", 
     "⚖️ Traditional vs Generative BI",
     "✅ Pros & Cons for Business",
     "🔧 Code Deep Dive",
     "🎯 Key Takeaways"])

# Introduction Section
if section == "🏠 Introduction":
    st.markdown("<h1 class='main-header'>Generative Business Intelligence (GenBI)</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #666;'>Transforming Data Analysis with AI-Powered Natural Language Processing</h3>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("📌 **This presentation explores how Generative BI revolutionizes data analysis by allowing users to interact with data using natural language, powered by Large Language Models (LLMs) like Claude.**")

# Theory Section
elif section == "📚 Theory: What is Generative BI?":
    st.markdown("<h2 class='section-header'>What is Generative Business Intelligence?</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Generative Business Intelligence (GenBI)** represents a paradigm shift in how organizations interact with their data. 
        It combines the power of:
        
        - 🤖 **Large Language Models (LLMs)** - Understanding natural language queries
        - 📊 **Traditional BI Tools** - Data visualization and analysis capabilities
        - 🔧 **Code Generation** - Automatically creating analysis scripts
        - 💡 **Natural Language Processing** - Bridging the gap between human intent and technical execution
        """)
    
    with col2:
        st.metric("Key Innovation", "Natural Language → Code", "Automatic Translation")
    
    st.markdown("### How GenBI Works")
    
    # Process flow
    process_df = pd.DataFrame({
        'Step': ['1️⃣ User Query', '2️⃣ LLM Processing', '3️⃣ Code Generation', '4️⃣ Execution', '5️⃣ Results'],
        'Description': [
            'User asks a question in plain English',
            'LLM interprets the intent and context',
            'Python/SQL code is generated automatically',
            'Code runs against the actual data',
            'Visualizations and insights are presented'
        ]
    })
    
    st.dataframe(process_df, use_container_width=True, hide_index=True)

# Comparison Section
elif section == "⚖️ Traditional vs Generative BI":
    st.markdown("<h2 class='section-header'>Traditional BI vs Generative BI</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Traditional BI")
        st.markdown("""
        <div class='traditional-bi-box comparison-box'>
        
        <strong>Characteristics:</strong>
        <ul>
            <li>Pre-built dashboards and reports</li>
            <li>Fixed metrics and KPIs</li>
            <li>Requires technical skills for modifications</li>
            <li>Limited flexibility for ad-hoc queries</li>
            <li>Time-consuming development cycle</li>
        </ul>
        
        <strong>Workflow:</strong>
        <ol>
            <li>Business defines requirements</li>
            <li>IT/Analytics team builds dashboards</li>
            <li>Users consume static reports</li>
            <li>Changes require new development cycle</li>
            <li>Often leads to "Excel export syndrome"</li>
        </ol>
        
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🚀 Generative BI")
        st.markdown("""
        <div class='generative-bi-box comparison-box'>
        
        <strong>Characteristics:</strong>
        <ul>
            <li>Natural language queries</li>
            <li>Dynamic, on-demand analysis</li>
            <li>No coding skills required for users</li>
            <li>Infinite flexibility for exploration</li>
            <li>Instant results and iterations</li>
        </ul>
        
        <strong>Workflow:</strong>
        <ol>
            <li>User asks question in plain English</li>
            <li>AI generates appropriate analysis</li>
            <li>Results delivered immediately</li>
            <li>User can refine or ask follow-ups</li>
            <li>True self-service analytics</li>
        </ol>
        
        </div>
        """, unsafe_allow_html=True)

# Pros and Cons Section
elif section == "✅ Pros & Cons for Business":
    st.markdown("<h2 class='section-header'>Business Impact: Pros & Cons</h2>", unsafe_allow_html=True)
    
    # Pros
    st.markdown("### ✅ Advantages")
    st.markdown("""
    <div class='pros-box'>
    
    <strong>1. 🔍 Superior Exploratory Analysis</strong>
    <ul>
        <li>Users can ask any question about their data without predefined limits</li>
        <li>Eliminates the "dashboard → Excel export → manual analysis" pattern</li>
        <li>Enables true data discovery and hypothesis testing</li>
    </ul>
    
    <strong>2. ⚡ Rapid Time-to-Insight</strong>
    <ul>
        <li>No waiting for dashboard development or modifications</li>
        <li>Questions answered in seconds, not days or weeks</li>
        <li>Iterative exploration becomes natural and efficient</li>
    </ul>
    
    <strong>3. 💰 Cost Efficiency</strong>
    <ul>
        <li>Reduces dependency on technical resources for basic analysis</li>
        <li>Minimizes redundant dashboard creation</li>
        <li>Democratizes data access across the organization</li>
    </ul>
    
    <strong>4. 🎯 User Empowerment</strong>
    <ul>
        <li>Business users can directly interrogate data</li>
        <li>No SQL or programming knowledge required</li>
        <li>Bridges the gap between business questions and technical execution</li>
    </ul>
    
    </div>
    """, unsafe_allow_html=True)
    
    # Cons
    st.markdown("### ❌ Challenges and Limitations")
    st.markdown("""
    <div class='cons-box'>
    
    <strong>1. 🎲 Inconsistency Risk</strong>
    <ul>
        <li>LLMs can generate different code for the same question</li>
        <li>Results may vary between runs (non-deterministic behavior)</li>
        <li>Critical for production environments requiring reproducibility</li>
    </ul>
    
    <strong>2. 🛡️ Quality Control</strong>
    <ul>
        <li>Generated code may not follow best practices</li>
        <li>Potential for inefficient or incorrect analysis</li>
        <li>Requires validation mechanisms for critical decisions</li>
    </ul>
    
    <strong>3. 🔒 Security Concerns</strong>
    <ul>
        <li>Natural language queries could expose sensitive data</li>
        <li>Need robust access controls and data governance</li>
        <li>Risk of unintended data exposure through generated queries</li>
    </ul>
    
    <strong>4. 📈 Scalability Questions</strong>
    <ul>
        <li>API costs can accumulate with heavy usage</li>
        <li>Performance considerations for large datasets</li>
        <li>Integration complexity with existing BI infrastructure</li>
    </ul>
    
    </div>
    """, unsafe_allow_html=True)

# Code Deep Dive Section
elif section == "🔧 Code Deep Dive":
    st.markdown("<h2 class='section-header'>Understanding the Implementation</h2>", unsafe_allow_html=True)
    
    # Code segment tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🤖 Claude Integration", "📝 Prompt Engineering", "🔄 Error Handling", "🎨 Visualization"])
    
    with tab1:
        st.markdown("### Claude API Integration")
        st.code("""
def ask_claude(prompt):
    '''
    This function takes a prompt and returns the response from Anthropic's Claude model.
    '''
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text
    except Exception as e:
        return f"An error occurred: {e}"
        """, language="python")
        
        st.markdown("""
        <div class='code-explanation'>
        <b>Key Points:</b><br>
        • Uses Claude Sonnet 4 - optimized for code generation<br>
        • 4000 max tokens allows for complex code responses<br>
        • Simple error handling ensures graceful failures<br>
        • Clean abstraction makes it easy to swap LLM providers
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### Intelligent Prompt Construction")
        st.code("""
def generate_python_code_prompt(df, question):
    START_CODE_TAG = "```"
    END_CODE_TAG = "```"
    num_rows, num_columns = df.shape
    columns_info = "\\n".join([f"{col}: {dtype}" for col, dtype in df.dtypes.items()])
    prompt = f'''
You are provided with a pandas dataframe (df) with {num_rows} rows and {num_columns} columns.
This is the metadata of the dataframe:
{columns_info}.

When asked about the data, your response should include the python code describing the
dataframe `df`. If the question requires data visualization, use Plotly for plotting...
'''
    return prompt
        """, language="python")
        
        st.markdown("""
        <div class='code-explanation'>
        <b>Smart Design Choices:</b><br>
        • Provides DataFrame context (shape, column types) to the LLM<br>
        • Uses code fence markers for reliable extraction<br>
        • Explicitly specifies Plotly for consistency<br>
        • Prevents common errors by mentioning 'df' variable name
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("### Self-Healing Code Execution")
        st.code("""
def execute_code(code, df, question, max_retries=5):
    error_message = None
    retries = 0
    
    while retries <= max_retries:
        try:
            exec_locals = {'df': df, 'px': px, 'go': go, 'pd': pd, 'np': np}
            exec(code, {}, exec_locals)
            # ... handle results ...
        except Exception as e:
            error_message = str(e)
            retries += 1
            if retries <= max_retries:
                # Ask Claude to fix the error
                new_formatted_prompt = f"... received this error message '{error_message}'..."
                output = ask_claude(new_formatted_prompt)
                code = extract_python_code(output)
        """, language="python")
        
        st.markdown("""
        <div class='code-explanation'>
        <b>Innovation: Self-Healing Capability</b><br>
        • Automatically retries failed code up to 5 times<br>
        • Sends error messages back to Claude for correction<br>
        • Creates a feedback loop for improved accuracy<br>
        • Significantly improves success rate for complex queries
        </div>
        """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("### Dynamic Visualization")
        st.markdown("""
        The system automatically:
        1. **Detects visualization needs** from natural language
        2. **Generates appropriate Plotly code** for the data type
        3. **Renders interactive charts** directly in Streamlit
        4. **Handles various chart types** (line, bar, scatter, etc.)
        
        Example user queries that trigger visualizations:
        - "Plot sales by month"
        - "Show me a histogram of customer ages"
        - "Create a scatter plot of price vs quantity"
        """)

# Key Takeaways Section
elif section == "🎯 Key Takeaways":
    st.markdown("<h2 class='section-header'>Key Takeaways & Recommendations</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🎯 When to Use Generative BI")
        st.success("""
        **Ideal Use Cases:**
        - Exploratory data analysis and discovery
        - Ad-hoc reporting and one-off questions
        - Proof of concepts and prototyping
        - Empowering non-technical users
        - Reducing dashboard proliferation
        """)
        
        st.markdown("### ⚠️ When to Use Traditional BI")
        st.warning("""
        **Better Suited For:**
        - Production reporting with strict SLAs
        - Regulatory compliance reports
        - Mission-critical dashboards
        - Scenarios requiring 100% reproducibility
        - High-frequency, automated reporting
        """)
    
    with col2:
        st.markdown("### 📊 Adoption Strategy")
        st.info("""
        **Recommended Approach:**
        
        1. **Pilot Phase**
           - Start with exploratory use cases
           - Train power users first
           
        2. **Expand Carefully**
           - Monitor accuracy and usage
           - Build trust gradually
           
        3. **Hybrid Model**
           - Use GenBI for exploration
           - Traditional BI for production
           
        4. **Continuous Improvement**
           - Refine prompts based on usage
           - Build a prompt library
        """)
    
    st.markdown("---")
    st.markdown("### 🚀 The Future of Business Intelligence")
    st.markdown("""
    Generative BI represents a fundamental shift in how organizations interact with data. While it won't replace 
    traditional BI entirely, it offers a powerful complementary approach that can:
    
    - **Accelerate** time-to-insight
    - **Democratize** data access
    - **Reduce** technical bottlenecks
    - **Enable** true self-service analytics
    
    The key to success lies in understanding both its capabilities and limitations, and deploying it strategically 
    where it can deliver the most value.
    """)
