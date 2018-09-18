import React from 'react';

class ContactAdd extends React.Component {
    constructor() {
        super();
        this.state = {
            contact: {}
        }
    }
}

// The ContactAdd function must not allow empty values, so an if statement must be added.

add_contact(event) {
    event.preventDefault();
    if (this.refs.name.value === '') {
        alert('Sorry, name cannot be empty')
    } else {
        this.setState({
            name: this.refs.name.value,
            number: this.refs.cellNumber.value,
            email: this.refs.email.value,
            address: this.refs.address.value,
            city: this.refs.city.value,
            state: this.refs.state.value,
            postal: this.refs.postal.value,
        }
    },
        function() {
            this.props.newContact(this.state.contact)
            
        }


