from gacp_agent_sdk import GACPSDK

# Order agent implementation
def order_agent_handler(task):
    """Order agent handler function"""
    task_type = task.get('type')
    if task_type == 'receive_order':
        # Receive order
        order_id = task.get('order_id')
        customer_info = task.get('customer_info')
        return {
            'status': 'success',
            'result': {
                'order_received': True,
                'order_id': order_id,
                'customer_info': customer_info,
                'status': 'pending_payment'
            }
        }
    elif task_type == 'update_order_status':
        # Update order status
        order_id = task.get('order_id')
        new_status = task.get('new_status')
        return {
            'status': 'success',
            'result': {
                'status_updated': True,
                'order_id': order_id,
                'new_status': new_status
            }
        }
    elif task_type == 'confirm_delivery':
        # Confirm delivery
        order_id = task.get('order_id')
        return {
            'status': 'success',
            'result': {
                'delivery_confirmed': True,
                'order_id': order_id,
                'status': 'completed'
            }
        }
    else:
        return {
            'status': 'error',
            'message': 'Unsupported task type'
        }

# Inventory agent implementation
def inventory_agent_handler(task):
    """Inventory agent handler function"""
    task_type = task.get('type')
    if task_type == 'check_inventory':
        # Check inventory
        product_id = task.get('product_id')
        quantity = task.get('quantity')
        # Simulate inventory check
        available_stock = 100  # Assume sufficient inventory
        return {
            'status': 'success',
            'result': {
                'inventory_checked': True,
                'product_id': product_id,
                'quantity_requested': quantity,
                'available_stock': available_stock,
                'sufficient': available_stock >= quantity
            }
        }
    elif task_type == 'update_inventory':
        # Update inventory
        product_id = task.get('product_id')
        quantity = task.get('quantity')
        return {
            'status': 'success',
            'result': {
                'inventory_updated': True,
                'product_id': product_id,
                'quantity_deducted': quantity
            }
        }
    else:
        return {
            'status': 'error',
            'message': 'Unsupported task type'
        }

# Shipping agent implementation
def shipping_agent_handler(task):
    """Shipping agent handler function"""
    task_type = task.get('type')
    if task_type == 'arrange_shipping':
        # Arrange shipping
        order_id = task.get('order_id')
        shipping_address = task.get('shipping_address')
        return {
            'status': 'success',
            'result': {
                'shipping_arranged': True,
                'order_id': order_id,
                'shipping_address': shipping_address,
                'tracking_number': f"SH{order_id[:8]}{task.get('timestamp', '')[-4:]}"
            }
        }
    elif task_type == 'track_delivery':
        # Track delivery
        tracking_number = task.get('tracking_number')
        return {
            'status': 'success',
            'result': {
                'delivery_tracked': True,
                'tracking_number': tracking_number,
                'status': 'in_transit',
                'estimated_delivery': '2024-03-20'
            }
        }
    else:
        return {
            'status': 'error',
            'message': 'Unsupported task type'
        }

# Payment agent implementation
def payment_agent_handler(task):
    """Payment agent handler function"""
    task_type = task.get('type')
    if task_type == 'process_payment':
        # Process payment
        order_id = task.get('order_id')
        amount = task.get('amount')
        payment_method = task.get('payment_method')
        return {
            'status': 'success',
            'result': {
                'payment_processed': True,
                'order_id': order_id,
                'amount': amount,
                'payment_method': payment_method,
                'transaction_id': f"TX{order_id[:8]}{task.get('timestamp', '')[-4:]}"
            }
        }
    elif task_type == 'handle_refund':
        # Handle refund
        order_id = task.get('order_id')
        amount = task.get('amount')
        reason = task.get('reason')
        return {
            'status': 'success',
            'result': {
                'refund_processed': True,
                'order_id': order_id,
                'amount': amount,
                'reason': reason,
                'refund_id': f"RF{order_id[:8]}{task.get('timestamp', '')[-4:]}"
            }
        }
    else:
        return {
            'status': 'error',
            'message': 'Unsupported task type'
        }

# Create and register agents
def create_ecommerce_fulfillment_agents():
    """Create agents for ecommerce fulfillment scenario"""
    # Create order agent
    order_agent = GACPSDK('order_agent', ['process_order', 'manage_order_status'])
    order_agent.register_task_handler(order_agent_handler)
    
    # Create inventory agent
    inventory_agent = GACPSDK('inventory_agent', ['check_inventory', 'update_inventory'])
    inventory_agent.register_task_handler(inventory_agent_handler)
    
    # Create shipping agent
    shipping_agent = GACPSDK('shipping_agent', ['arrange_shipping', 'track_delivery'])
    shipping_agent.register_task_handler(shipping_agent_handler)
    
    # Create payment agent
    payment_agent = GACPSDK('payment_agent', ['process_payment', 'handle_refunds'])
    payment_agent.register_task_handler(payment_agent_handler)
    
    return [order_agent, inventory_agent, shipping_agent, payment_agent]

if __name__ == '__main__':
    # Example usage
    agents = create_ecommerce_fulfillment_agents()
    print("Ecommerce fulfillment scenario agents created successfully:")
    for agent in agents:
        print(f"- {agent.agent_id}: {agent.capabilities}")
