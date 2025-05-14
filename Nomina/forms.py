from django import forms
from .models import Empleado, Rol, Cargo,  Departamento, TipoContrato, Prestamo
from django.forms import ModelForm, TextInput, EmailInput, NumberInput, Select,Textarea

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre completo del empleado'}),
            'cedula': TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12.345.678'}),
            'sexo': Select(attrs={'class': 'form-select'}, choices=[('', 'Seleccione género'), ('M', 'Masculino'), ('F', 'Femenino')]),
            'direccion': Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': 'Dirección completa del empleado'}),
            'sueldo': NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'placeholder': '0.00'}),
            'cargo': Select(attrs={'class': 'form-select'}),
            'departamento': Select(attrs={'class': 'form-select'}),
            'tipo_contrato': Select(attrs={'class': 'form-select'})
        }
        



class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'
        
class TipoContratoForm(forms.ModelForm):
    class Meta:
        model = TipoContrato
        fields = '__all__'
        


class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        exclude = ['sueldo', 'iess', 'tot_ing', 'tot_des', 'neto']
        widgets = {
            'aniomes': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'empleado': forms.Select(attrs={'class': 'form-select'}),
            'horas_extras': forms.NumberInput(attrs={'type': 'number', 'class': 'form-control', 'min': 0, 'step': '0.01'}),
            'bono': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'step': '0.01'}),
        }
        
        
class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = '__all__'
        widgets = {
            'empleado': forms.Select(attrs={'class': 'form-select'}),
            'tipo_prestamo': forms.Select(attrs={'class': 'form-select'}),
            'fecha_prestamo': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'interes': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'monto_pagar': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'numero_cuotas': forms.NumberInput(attrs={'class': 'form-control'}),
            'cuota_mensual': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
            'saldo': forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}),
        }
        
        