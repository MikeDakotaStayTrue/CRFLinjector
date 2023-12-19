from javax.swing import JPanel, JButton, JTextField, JFrame, BorderFactory, JLabel, GroupLayout, JToggleButton, JCheckBox, SwingConstants, JSeparator
from java.awt import BorderLayout, GridLayout, FlowLayout
from java.awt import Dimension, Font, Color

import logging

class GUI:
    def __init__(self, burp_extender):
        self._extender = burp_extender
        self._main_panel = JPanel()
        self._panel = JPanel()
        self._show_nonce = True
        self._nonce_curr_lbl = JTextField("")
        self._nonce_curr_lbl.setEditable(False)


    def get_main_panel(self):
        return self._main_panel

    def create_gui(self):

        def click_save(event):
            self._extender.set_header_value(header_value_text.getText())
            self._extender.set_header_name(header_name_text.getText())
            return
        
        ###################
        # Init components #
        ###################

        banner = JLabel("CRLF Injector")
        banner_font = banner.getFont().getName()
        banner.setFont(Font(banner_font, Font.BOLD, 24))
    
        label_header_name = JLabel("Add header for injection")
        banner_font = banner.getFont().getName()
        banner.setFont(Font(banner_font, Font.BOLD, 18))

        header_name_label = JLabel("Name")
        header_name_text = JTextField(self._extender.get_header_name())
        header_name_text.setPreferredSize(Dimension(400,1))

        header_value_label = JLabel("Value")
        header_value_text = JTextField(self._extender.get_header_value())
        header_value_text.setPreferredSize(Dimension(400,1))


        button_save = JButton("Save", actionPerformed=click_save)


        # Init layout
        layout = GroupLayout(self._panel)
        self._panel.setLayout(layout)
        layout.setAutoCreateGaps(True)
        layout.setAutoCreateContainerGaps(True)
 


        # Add components to center parallel group
        hGroup = layout.createParallelGroup(GroupLayout.Alignment.CENTER)
        hGroup.addComponent(banner)
        hGroup.addComponent(label_header_name)

        hGroup.addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                     .addComponent(header_name_label)
                     .addComponent(header_value_label)
                     .addComponent(button_save))

                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                    .addComponent(header_name_text)
                    .addComponent(header_value_text)))

        # Add components to horizontal group
        layout.setHorizontalGroup(hGroup)
        vGroup = layout.createSequentialGroup()
        vGroup.addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup()
                    .addComponent(banner))
                .addGroup(layout.createParallelGroup()
                    .addComponent(label_header_name))
                .addGroup(layout.createParallelGroup()
                    .addComponent(header_name_label)
                    .addComponent(header_name_text))
                .addGroup(layout.createParallelGroup()
                    .addComponent(header_value_label)
                    .addComponent(header_value_text))
                .addGroup(layout.createParallelGroup()
                    .addComponent(button_save))
                )

        layout.setVerticalGroup(vGroup)
        self._main_panel.add(self._panel)