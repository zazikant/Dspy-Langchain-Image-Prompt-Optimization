sub Agents:

1.  **task folder**: Contains Product Requirement Documents (PRDs) and their implementation plans.
2.  **system folder**: Houses overarching architectural and structural information (e.g., project structure, database schemas, API specifications).
3.  **SOPs folder**: Stores Standard Operating Procedures and logs of past mistakes.
4. Readme.md: Your README.md might say:"Welcome to our restaurant operation system. We have three main sections...""Task Folder: Find daily prep instructions and event planning here""System Folder: Our menu structure, supplier list, and floor layout are here""SOPs Folder: Lessons from past mistakes and how to handle problems — located here"

also,if the main agent is instructed to look at .agents folder first (just like the sub-agents), that folder could contain a file that lists: "Available sub-agents: SubAgent1.md, SubAgent2.md" with details on what each one does


Question: Lets say I have a langgraph agent and a node has a code that does a input as email id and output as 10 different fields of operations. Will this node code be a task? Will it be a sop? Will it be a system folder?

Answer:

Great question! Let me break this down for your specific scenario.

That node code would actually be **part of the System folder**, not a task or SOP.

Here's why:

**System Folder** is where you'd document this because it describes *how your agent works structurally*. It's architectural information — "We have a node that takes an email ID and extracts 10 operational fields from it." This is like the blueprint of your restaurant's payment processing system or how orders flow through the kitchen.

**Now, here's where the other folders come in:**

**Task Folder** would contain *what you want the agent to do with that node*. For example: "Task: Extract customer information from email database. Expected outcome: Get 10 fields for 500 customers by end of day." This is the *instruction* to use that node, not the node itself.

**SOPs Folder** would contain lessons learned, like: "We discovered that email IDs sometimes have special characters — here's how to handle them to avoid errors" or "When the extraction fails on certain emails, here's the fallback process we use now."

So to summarize:
- **System**: "We have a node that processes email IDs → outputs 10 fields"
- **Task**: "Go process these 100 email IDs and extract those 10 fields"
- **SOPs**: "Here's what we learned when it breaks, and here's our procedure to fix it"

Does that distinction make sense?
