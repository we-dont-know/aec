#Incident report prog5 part B
class SecurityIncident:
    def _init_(self, incident_type, description):
        self.incident_type = incident_type
        self.description = description

    def _str_(self):
        return f"type: {self.incident_type}, description: {self.description}"
    
class IncidentReporter:
    def _init_(self):
        self.incidents = []

    def report_incident(self, incident_type, description):
        incident = SecurityIncident(incident_type, description)
        self.incidents.append(incident)
        print("Incident reported successfully")

    def show_reports(self):
        if not self.incidents:
            print("No incidents reported")
        else:
            for idx, incident in enumerate(self.incidents, 1):
                print(f"Incident {idx}: {incident}")

def main():
    reporter = IncidentReporter()
    while True:
        print("\nSecurity Incident Reporting Tool")
        print("1: Report an incident\n2: Show incidents\n3: Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            incident_type = input("Enter the type of incident (e.g., lost device, suspicious email): ")
            description = input("Enter the description of the incident: ")
            reporter.report_incident(incident_type, description)
        elif choice == '2':
            reporter.show_reports()
        elif choice == '3':
            print("Exiting the tool")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
