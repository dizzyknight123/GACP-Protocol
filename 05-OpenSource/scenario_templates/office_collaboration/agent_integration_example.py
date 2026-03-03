from gacp_agent_sdk import GACPSDK

# Calendar agent implementation
def calendar_agent_handler(task):
    """Calendar agent handler function"""
    task_type = task.get('type')
    if task_type == 'analyze_meeting_requirements':
        # Analyze meeting requirements and return time suggestions
        return {
            'status': 'success',
            'result': {
                'meeting_time_suggestions': [
                    '2024-03-15 10:00-11:00',
                    '2024-03-15 14:00-15:00',
                    '2024-03-16 09:00-10:00'
                ]
            }
        }
    elif task_type == 'schedule_meeting':
        # Schedule meeting time
        meeting_time = task.get('meeting_time')
        participants = task.get('participants')
        return {
            'status': 'success',
            'result': {
                'meeting_scheduled': True,
                'meeting_time': meeting_time,
                'participants': participants
            }
        }
    else:
        return {
            'status': 'error',
            'message': 'Unsupported task type'
        }

# Document agent implementation
def document_agent_handler(task):
    """Document agent handler function"""
    task_type = task.get('type')
    if task_type == 'create_meeting_document':
        # Create meeting document
        meeting_topic = task.get('meeting_topic')
        return {
            'status': 'success',
            'result': {
                'document_created': True,
                'document_id': 'doc_{}'.format(meeting_topic.replace(' ', '_')),
                'document_content': f"# {meeting_topic}\n\n## Agenda\n\n## Discussion Points\n\n## Action Items"
            }
        }
    elif task_type == 'organize_meeting_notes':
        # Organize meeting notes
        meeting_id = task.get('meeting_id')
        return {
            'status': 'success',
            'result': {
                'notes_organized': True,
                'meeting_id': meeting_id,
                'notes': "# Meeting Notes\n\n## Discussion Content\n\n## Decisions\n\n## Action Items"
            }
        }
    else:
        return {
            'status': 'error',
            'message': 'Unsupported task type'
        }

# Communication agent implementation
def communication_agent_handler(task):
    """Communication agent handler function"""
    task_type = task.get('type')
    if task_type == 'send_meeting_invite':
        # Send meeting invitation
        participants = task.get('participants')
        meeting_details = task.get('meeting_details')
        return {
            'status': 'success',
            'result': {
                'invites_sent': True,
                'participants': participants,
                'meeting_details': meeting_details
            }
        }
    elif task_type == 'send_meeting_reminder':
        # Send meeting reminder
        participants = task.get('participants')
        meeting_time = task.get('meeting_time')
        return {
            'status': 'success',
            'result': {
                'reminders_sent': True,
                'participants': participants,
                'meeting_time': meeting_time
            }
        }
    elif task_type == 'distribute_meeting_notes':
        # Distribute meeting notes
        participants = task.get('participants')
        notes = task.get('notes')
        return {
            'status': 'success',
            'result': {
                'notes_distributed': True,
                'participants': participants
            }
        }
    else:
        return {
            'status': 'error',
            'message': 'Unsupported task type'
        }

# Create and register agents
def create_office_collaboration_agents():
    """Create agents for office collaboration scenario"""
    # Create calendar agent
    calendar_agent = GACPSDK('calendar_agent', ['schedule_meeting', 'manage_calendar'])
    calendar_agent.register_task_handler(calendar_agent_handler)
    
    # Create document agent
    document_agent = GACPSDK('document_agent', ['create_document', 'edit_document'])
    document_agent.register_task_handler(document_agent_handler)
    
    # Create communication agent
    communication_agent = GACPSDK('communication_agent', ['send_email', 'manage_messages'])
    communication_agent.register_task_handler(communication_agent_handler)
    
    return [calendar_agent, document_agent, communication_agent]

if __name__ == '__main__':
    # Example usage
    agents = create_office_collaboration_agents()
    print("Office collaboration scenario agents created successfully:")
    for agent in agents:
        print(f"- {agent.agent_id}: {agent.capabilities}")
