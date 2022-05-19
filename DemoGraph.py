
graphs = {
    "Overview": """
        digraph {
            graph [label="XECO11587_QF0406_D01_Master_Data_Change_Request_V02 - Overview" layout=circo]
            node [border=3 fontname=Arial shape=record style=filled]
            091.4124 [label="091.4124.110\nB04 &gt; B05\nMR X Motor Cable" fillcolor="#A0F0ED" fontcolor=Black]
            091.4204 [label="091.4204.110\nC01 &gt; C02\nSlide IO Opto Cable" fillcolor="#A0F0ED" fontcolor=Black]
            091.4095 [label="091.4095.110\nD01 &gt; D02\nSpeaker Cable" fillcolor="#A0F0ED" fontcolor=Black]
            091.5571 [label="091.5571.130\nF02 &gt; F03\nRobot Head PWA\nDrawing not found in Artifactory" fillcolor="#A0F0ED" fontcolor=Black]
            "S091.4204" [label="S091.4204.000\nA01\nSlide Drawer Opto" fillcolor=White fontcolor=Black]
            091.0343 [label="091.0343.000\nS01\n*Robot Head Assembly" fillcolor=White fontcolor=Black]
            "S091.5571" [label="S091.5571.000\nA01\nRobot Head PWA" fillcolor=White fontcolor=Black]
            091.4204 -> "S091.4204" [fontname=Arial label=""]
            091.5571 -> 091.0343 [fontname=Arial label=""]
            091.5571 -> "S091.5571" [fontname=Arial label=""]
        }
    """,
    "S091.4204": """
        digraph {
            graph [label="XECO11587_QF0406_D01_Master_Data_Change_Request_V02 - S091.4204" layout=dot rankdir=LR]
            node [border=3 fontname=Arial shape=record style=filled]
            "S091.4204" [label="S091.4204.000\nA01\nSlide Drawer Opto" fillcolor=White fontcolor=Black]
            091.4204 [label="091.4204.110\nC01 &gt; C02\nSlide IO Opto Cable" fillcolor="#A0F0ED" fontcolor=Black]
            091.4204 -> "S091.4204" [fontname=Arial label=""]
        }
    """,
    "091.0343":"""
        digraph {
            graph [label="XECO11587_QF0406_D01_Master_Data_Change_Request_V02 - 091.0343" layout=dot rankdir=LR]
            node [border=3 fontname=Arial shape=record style=filled]
            091.0343 [label="091.0343.000\nS01\n*Robot Head Assembly" fillcolor=White fontcolor=Black]
            091.5571 [label="091.5571.130\nF02 &gt; F03\nRobot Head PWA\nDrawing not found in Artifactory" fillcolor="#A0F0ED" fontcolor=Black]
            091.5571 -> 091.0343 [fontname=Arial label=""]
        }
    """,
    "S091.5571": """
    digraph {
        graph [label="XECO11587_QF0406_D01_Master_Data_Change_Request_V02 - S091.5571" layout=dot rankdir=LR]
        node [border=3 fontname=Arial shape=record style=filled]
        "S091.5571" [label="S091.5571.000\nA01\nRobot Head PWA" fillcolor=White fontcolor=Black]
        091.5571 [label="091.5571.130\nF02 &gt; F03\nRobot Head PWA\nDrawing not found in Artifactory" fillcolor="#A0F0ED" fontcolor=Black]
        091.5571 -> "S091.5571" [fontname=Arial label=""]
    }
    """,
    "orphans" : """
        digraph {
            graph [label="XECO11587_QF0406_D01_Master_Data_Change_Request_V02 - Other" layout=dot rankdir=LR]
            node [border=3 fontname=Arial shape=record style=filled]
            091.4124 [label="091.4124.110\nB04 &gt; B05\nMR X Motor Cable" fillcolor="#A0F0ED" fontcolor=Black]
            091.4095 [label="091.4095.110\nD01 &gt; D02\nSpeaker Cable" fillcolor="#A0F0ED" fontcolor=Black]
    }"""
}

