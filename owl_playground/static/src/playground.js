/** @odoo-module **/

import { Counter } from "./counter";
import { Component } from "@odoo/owl";


export class Playground extends Component {
    static template = "owl_playground.playground";

    static components = { Counter };
}


