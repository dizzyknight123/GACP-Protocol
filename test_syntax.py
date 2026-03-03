import sys
sys.path.append('02-Core-Code')

try:
    from gacp_mvp import GACPMVP
    print('GACP MVP imported successfully')
    
    from requirement_parser import RequirementParser
    print('Requirement Parser imported successfully')
    
    from contract_generator import ContractGenerator
    print('Contract Generator imported successfully')
    
    from task_router import TaskRouter
    print('Task Router imported successfully')
    
    from trust_validator import TrustValidator
    print('Trust Validator imported successfully')
    
    print('All core modules imported successfully, code syntax is correct')
except Exception as e:
    print(f'Import failed: {e}')
    sys.exit(1)