from bokeh.plotting import figure, show


class BarChart:
    def bar_chart(db_data, bar_chart_title: str, x_label: str, y_label: str) -> figure:
        """
        Generate bar chart based on the database information.
        Params:
            1. DB information after the connection and query made.
            2. The title user wants to give to bar chart (e.g: "5 best salesperson.").
            3. Label x_axis data (e.g: "Employee's Name").
            4. Label y_axis data (e.g: "Total Sales"). 
        Returns:
            bar_chart figure.
        """
        x_axis, y_axis = db_data

        p = figure(x_range=x_axis, 
                height=350, 
                title=bar_chart_title, 
                x_axis_label=x_label,
                y_axis_label=y_label)

        p.vbar(x=x_axis, top=y_axis, width=0.6)

        p.xaxis.major_label_orientation = "vertical"
        p.y_range.start = 0

        show(p)

