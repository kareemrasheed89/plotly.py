import _plotly_utils.basevalidators


class TicklabelpositionValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="ticklabelposition",
        parent_name="isosurface.colorbar",
        **kwargs
    ):
        super(TicklabelpositionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop(
                "values",
                [
                    "outside",
                    "inside",
                    "outside top",
                    "inside top",
                    "outside bottom",
                    "inside bottom",
                ],
            ),
            **kwargs
        )
