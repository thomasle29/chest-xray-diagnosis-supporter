import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Base64toimgComponent } from './base64toimg.component';

describe('Base64toimgComponent', () => {
  let component: Base64toimgComponent;
  let fixture: ComponentFixture<Base64toimgComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Base64toimgComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(Base64toimgComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
