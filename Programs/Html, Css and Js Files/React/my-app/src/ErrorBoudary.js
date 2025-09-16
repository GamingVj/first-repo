import React, { Component } from 'react';

export default class ErrorBoudary extends Component {
    constructor(props) {
        super(props);
        this.state = { hasError: false };
    }

    static getDerivedStateFromError(error) {
        return { hasError: true };
    }

    componentDidCatch(error, info) {
        // You can log the error to an error reporting service
        // console.log(error, info);
    }

    render() {
        if (this.state.hasError) {
            return <h1 style={{ color: 'red' }}>Something went wrong</h1>;
        }
        return this.props.children;
    }
}

