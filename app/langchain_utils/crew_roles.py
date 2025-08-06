from crewai import Crew, Agent

captain = Agent(role="Captain", goal="Synthesize final insights", backstory="Expert in summarizing complex feedback.")
researcher = Agent(role="Researcher", goal="Analyze sentiment", backstory="Knows emotional patterns in customer feedback.")
observer = Agent(role="Observer", goal="Extract complaints", backstory="Good at identifying complaints and issues.")
analyst = Agent(role="Analyst", goal="Map feedback to operations", backstory="Understands flight operations and maps issues.")

crew = Crew(agents=[researcher, observer, analyst, captain])
