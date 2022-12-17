from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window
Window.size = (800, 700)


class FileChoosePopup(Popup):
    load = ObjectProperty()


class Tab(TabbedPanel):
    file_path = StringProperty("No file chosen")
    the_popup = ObjectProperty(None)

    def get_file(self):
        download_path = self.file_chooser.path
    
    def open_popup_source(self):
        self.the_popup = FileChoosePopup(load=self.load_source)
        self.the_popup.open()
 
    def load_source(self, selection):
        self.file_path = str(selection[0])
        self.the_popup.dismiss()
        print(self.file_path)

        # check for non-empty list i.e. file selected
        if self.file_path:
            self.ids.DATA_FOLDER.text = self.file_path

    def open_popup_export(self):
        self.the_popup = FileChoosePopup(load=self.load_export)
        self.the_popup.open()

    def load_export(self, selection):
        self.file_path = str(selection[0])
        self.the_popup.dismiss()
        print(self.file_path)

        # check for non-empty list i.e. file selected
        if self.file_path:
            self.ids.SAVE_DATA_FOLDER.text = self.file_path

class FileApp(App):

    def build(self):
        return Tab()
    
    def submit(self):
        print("Submit button has been pressed")
        
        """ Basic """
        series_name_value = self.root.ids.series_name.text
        if series_name_value:
            self.root.ids.series_name_label.text = f"Series name: {series_name_value}"
        
        DATA_FOLDER_value = self.root.ids.DATA_FOLDER.text
        if DATA_FOLDER_value:
            self.root.ids.DATA_FOLDER_label.text = f"Data source folder: {DATA_FOLDER_value}"
        
        SAVE_DATA_FOLDER_value = self.root.ids.SAVE_DATA_FOLDER.text
        if SAVE_DATA_FOLDER_value:
            self.root.ids.SAVE_DATA_FOLDER_label.text = f"Data export folder: {SAVE_DATA_FOLDER_value}"
        
        NUM_CELLS_value = self.root.ids.NUM_CELLS.text
        if NUM_CELLS_value:
            self.root.ids.NUM_CELLS_label.text = f"NUM_CELLS: {NUM_CELLS_value}"
        
        FRAMES_COUNT_value = self.root.ids.FRAMES_COUNT.text
        if FRAMES_COUNT_value:
            self.root.ids.FRAMES_COUNT_label.text = f"Number of frames: {FRAMES_COUNT_value}"
        
        """ Advanced """
        PHOTO_WEIGHT_value = self.root.ids.PHOTO_WEIGHT.text
        if PHOTO_WEIGHT_value:
            self.root.ids.PHOTO_WEIGHT_label.text = f"PHTOTO_WEIGHT: {PHOTO_WEIGHT_value}"
        
        PHOTO_DURATION_value = self.root.ids.PHOTO_DURATION.text
        if PHOTO_DURATION_value:
            self.root.ids.PHOTO_DURATION_label.text = f"PHOTO_DURATION: {PHOTO_DURATION_value}"
        
        BASED_ON_PHOTOS_value = self.root.ids.BASED_ON_PHOTOS.text
        if BASED_ON_PHOTOS_value:
            self.root.ids.BASED_ON_PHOTOS_label.text = f"BASED_ON_PHOTOS: {BASED_ON_PHOTOS_value}"
        
        SPEED_value = self.root.ids.SPEED.text
        if SPEED_value:
            self.root.ids.SPEED_label.text = f"SPEED: {SPEED_value}"
        
        SENSOR_DISTANCE_value = self.root.ids.SENSOR_DISTANCE.text
        if SENSOR_DISTANCE_value:
            self.root.ids.SENSOR_DISTANCE_label.text = f"SENSOR_DISTANCE: {SENSOR_DISTANCE_value}"
        
        SENSOR_ANGLE_value = self.root.ids.SENSOR_ANGLE.text
        if SENSOR_ANGLE_value:
            self.root.ids.SENSOR_ANGLE_label.text = f"SENSOR_ANGLE: {SENSOR_ANGLE_value}"
        
        ROTATE_ANGLE_value = self.root.ids.ROTATE_ANGLE.text
        if ROTATE_ANGLE_value:
            self.root.ids.ROTATE_ANGLE_label.text = f"ROTATE_ANGLE: {ROTATE_ANGLE_value}"
        
        VSIM_CELL_WEIGHT_value = self.root.ids.VSIM_CELL_WEIGHT.text
        if VSIM_CELL_WEIGHT_value:
            self.root.ids.VSIM_CELL_WEIGHT_label.text = f"VSIM_CALL_WEIGHT: {VSIM_CELL_WEIGHT_value}"
        
        VSIM_LIFETIME_value = self.root.ids.VSIM_LIFETIME.text
        if VSIM_LIFETIME_value:
            self.root.ids.VSIM_LIFETIME_label.text = f"VSIM_LIFETIME: {VSIM_LIFETIME_value}"

    
    def reset(self):
        print("Reset button has been pressed")

    def generate(self):
        print("I want to generate sequence")

FileApp().run()